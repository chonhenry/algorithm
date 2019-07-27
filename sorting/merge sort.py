from random import randrange

def mergeSort(arr):
	if len(arr)==1:
		return arr
	else:
		middle = len(arr)//2
		left = arr[:middle]
		right = arr[middle:]
		return merge(mergeSort(left),mergeSort(right))


def merge(left, right):
	result = []
	leftIndex = 0
	rightIndex = 0

	while (leftIndex<len(left) and rightIndex<len(right)):
		if right[rightIndex] < left[leftIndex]:
			result.append(right[rightIndex])
			rightIndex+=1
		else:
			result.append(left[leftIndex])
			leftIndex+=1

	return result + left[leftIndex:] + right[rightIndex:]


arr = []
for i in range(20):
	arr.append(randrange(100))
print(arr)

print(mergeSort(arr))


from random import randrange

def quickSort(arr, low, high):
	if low < high:
		pi = partition(arr, low, high)
		
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

def partition(arr, low, high):
	pivot = high
	i = low
	while(i != pivot):
		if arr[i] > arr[pivot]:
			temp = arr[pivot]
			arr[pivot] = arr[i]
			arr[i] = arr[pivot-1]
			arr[pivot-1] = temp
			pivot-=1
		else:
			i+=1
	return pivot

arr = []
for i in range(20):
	arr.append(randrange(100))
print(arr)

quickSort(arr, 0, len(arr)-1)
print(arr)




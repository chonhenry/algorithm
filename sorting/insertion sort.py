numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def InsertionSort(arr):
	for i in range(1, len(arr)):
		for j in range(i-1,-1,-1):
			if arr[i]<arr[j]:
				temp = arr[i]
				arr[i] = arr[j]
				arr[j] = temp
			i-=1
	return arr


print(InsertionSort(numbers))


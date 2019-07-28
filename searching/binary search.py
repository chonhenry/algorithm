def binarySearch(arr, low, high, x):
	while low <= high:
		mid = (high+low)//2

		if arr[mid] == x:
			return 'The index of ' + str(x) + ' is ' + str(mid)
		elif x < arr[mid]:
			high = mid - 1
		else:
			low = mid + 1

	return -1

arr = [1,4,5,8,10,14,19,21,26,30]

for i in arr:
	print(binarySearch(arr, 0, len(arr)-1, i))


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def SelectionSort(lst):
	for i in range(0,len(lst)):
		smallest = i
		temp = lst[i]
		for j in range(i+1,len(lst)):
			if lst[j]<lst[smallest]:
				smallest=j
		lst[i]=lst[smallest]
		lst[smallest]=temp

	return lst

print(SelectionSort(numbers))
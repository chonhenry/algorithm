numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def BubbleSort(lst):
	l = len(lst)

	for i in range(len(lst)-1):
		for j in range(len(lst)-1):
			if lst[j] > lst[j+1]:
				temp = lst[j]
				lst[j] = lst[j+1]
				lst[j+1] = temp

	return lst

print(BubbleSort(numbers))

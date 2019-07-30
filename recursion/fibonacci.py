def fib(n):
	if n==1 or n==2:
		return 1
	elif n>2:
		return fib(n-1)+fib(n-2)

def fib_seq(n): #print the entire sequence
	arr = []
	for i in range(1,n+1):
		arr.append(fib(i))

	return arr

def main():
	print(fib(13))
	print('=============')
	print(fib_seq(13))

main()




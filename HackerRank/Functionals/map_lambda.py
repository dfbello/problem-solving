# Python Functionals

cube = lambda x: x**3

def fib(n):
	if n == 1:
		return 0
	if n == 2:
		return 1
	if n > 2:
		return fib(n-1) + fib(n-2)

def fibonacci(n):
	for i in range(1, n+1):
		yield fib(i)


		

n = int(input())
print(list(map(cube, fibonacci(n))))

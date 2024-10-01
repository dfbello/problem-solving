# Errors and exceptions - exceptions

def errorDiv(a, b):

	try:
		print(int(a)/int(b))
	except ZeroDivisionError as e:
		print("Error Code:", "integer division or modulo by zero")
	except ValueError as e:
		print("Error Code:", e)

with open("./input.txt", "r") as file:

	T = int(file.readline())

	for i in range(T):
		a, b = file.readline().split()
		errorDiv(a,b)


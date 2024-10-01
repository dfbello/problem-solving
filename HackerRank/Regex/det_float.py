# Regex an Parsing - Detect floating point number
import re

def isFloat(n):

	match = re.match(r'[-+]?\d*\.\d+', n) 

	if match is None:
		return False
	elif match.group() != n:
		return False

	return True



with open("./input.txt", "r") as file:

	T = int(file.readline())
	for _ in range(T):
		N = file.readline().strip()
		print(isFloat(N))





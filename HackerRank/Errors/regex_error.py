# Errors and Exceptions - incorrect regex

import re

with open("./input.txt", "r") as file:

	T = int(file.readline())
	regex_list = []
	for _ in range(T):
		try:
			x = re.compile(r"%s" % file.readline().strip())
			print(True)
		except re.error as _:
			print(False)

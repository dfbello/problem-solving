# Collections - word order

from collections import OrderedDict

od = OrderedDict()

with open("./input.txt", "r") as file:

	N = int(file.readline())
	for i in range(N):


		s = file.readline()
		if s in od:
			od[s] += 1
		else:
			od[s] = 1

print(len(od.items()))
print(*od.values())
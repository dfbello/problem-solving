# Collections - Pilling up

from collections import deque
from itertools import groupby

def isStackable(d):

	while len(d) > 1:
		if max(d) not in [d[0], d[-1]]:
			return "No"

		if d[0] > d[-1]:
			d.popleft()
		else:
			d.pop()

	return "Yes"



with open("./input2.txt", "r") as file:

	T = int(file.readline())
	for i in range(T):
		_ = file.readline()
		ls = list(map(int, file.readline().split()))
		grouped = groupby(ls)
		dq = deque([x for x, _ in grouped])
		
		print(isStackable(dq))
		








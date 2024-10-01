# Collections - Default Dict tuto

from collections import defaultdict as dfd

with open("./input.txt") as file:

	n, m = map(int, file.readline().split())
	grp_a = []
	grp_b = []

	for i in range(n):
		grp_a.append(file.readline().rstrip())

	for i in range(m):
		grp_b.append(file.readline().rstrip())

d = dfd(list)

for i, x in enumerate(grp_a, start=1):
	if x in grp_b:
		d[x].append(i) 

for v in grp_b:
	if v in grp_a:
		print(*d[v])
	else:
		print(-1)

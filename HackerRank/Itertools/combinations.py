# Itertools - combinations

from itertools import combinations as cb

s, k = input().split()
s, k = list(s), int(k)

combi = []
res = []

s.sort()

for i in range(1, k+1):

	l = list(cb(s,i))

	combi = [*combi, *l]



for x in combi:
	res.append("".join(x))



print("\n".join(res))

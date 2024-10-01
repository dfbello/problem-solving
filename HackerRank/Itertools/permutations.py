# Itertools - permutations


from itertools import permutations as perm

s, k = input().split()
s, k = list(s), int(k)

s.sort()

combi = list(perm(s, k))
res = []


for x in combi:
	res.append("".join(x))



print("\n".join(res))

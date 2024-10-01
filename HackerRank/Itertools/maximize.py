#Itertools - maximize it

import itertools as it

def powersum(*args):
	ls = [x**2 for x in args]
	return sum(ls)%M


with open("./input.txt", "r") as file:

	K, M = map(int, file.readline().split())
	lists = []

	for i in range(K):
		N, ls = file.readline().split(" ", 1)
		N, ls = int(N), list(map(int, ls.split()))
		lists.append(ls)


res = list(it.starmap(powersum, list(it.product(*lists))))

print(max(res))




		



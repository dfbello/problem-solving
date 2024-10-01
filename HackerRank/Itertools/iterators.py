# itertools - iterators and itreables
import itertools as it


with open("./input.txt", "r") as f:
	N = int(f.readline())
	ls = f.readline().split()
	K = int(f.readline())

combs = list(it.combinations(ls , K))

count = 0

for c in combs:
	if "a" in c:
		count += 1






print(count/len(combs))

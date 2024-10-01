# Itertools - Compress the string

#Itertools - Compress
from itertools import groupby

s = input()

groups = groupby(s)
res = []

for key, g in groups:
	res.append((len(list(g)), int(key)))
	
print(*res)





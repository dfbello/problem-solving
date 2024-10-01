# Regex and parsing - re.start() & re.end()
import re


s = "aabcdeffgabcdef"
k = "abcdef"

exp = re.compile("(?=(%s))" % k)
check = exp.search(s)

if check:
	found = exp.finditer(s)

	for x in found:
		st = x.start()
		print((st, st + len(k) -1 ))
else:
	print((-1,-1))



	






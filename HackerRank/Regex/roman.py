# Regex and Parsing - Roman numbers

import re 

s = "XIM"

exp = re.compile(r'^[IXCM]{,3}$')

match = exp.match(s)

if match:
	print(match.group())
else:
	print(-1)
# Regex and Parsing - group() groups() and groupdict()
import re

s = "--init--"

search = re.search(r'([\da-zA-Z])\1{1,}', s)
if search is None:
	print(-1)
else:
	print(search.groups()[0])

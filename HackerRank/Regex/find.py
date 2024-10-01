# Regex and Parsing - findall() and finditer()

import re

s = "abaabaabaabaae"

matches = re.findall(r'(?<=[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z])[aeiouAEIOU]{2,}(?=[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z])', s)


if len(matches) == 0:
	print(-1)
else:
	print("\n".join(matches))
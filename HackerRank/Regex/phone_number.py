# Regex and Parsing - Validating phone numbers

import re

s = "6123456789"


def validate(s):

	exp = re.compile(r'^[789][\d]{9}$')
	match = exp.match(s)

	if match:
		print("YES")
	else:
		print("NO")

validate(s)

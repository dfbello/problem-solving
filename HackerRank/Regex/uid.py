# Regex and Parsing - Validating UID

import re

def validate(s):

	exp = re.compile(r'(?=[A-Z][a-z][0-9]{10}$)(?=.*?[A-Z]{2,})(?=.*?[0-9]{3,}).*')
	match = exp.match(s)

	if match:
		print("Valid")
	else:
		print("Invalid")


s = "b1AcA23543"

validate(s)
# Regex an Parsing - Hex color code 

import re

def validate_hex(s):
	
	exp = re.compile(r'(?<!\n)#[a-fA-F0-9]{3,6}')
	check = exp.search(s)

	if check:

		matches = exp.finditer(s)
		for match in matches:

			print(match.group())






with open("./input.txt", "r") as file:

	content = file.read()


validate_hex(content)
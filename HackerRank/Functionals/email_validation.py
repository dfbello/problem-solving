# Python Functionals - Validating an email address

import re

s = "imdiegob@gmail.com"

pat = re.compile(r'^(?P<username>[\w-]+)@(?P<domain>[a-zA-Z0-9]+)\.(?P<extension>[a-zA-Z]{1,3})$')

x = pat.match(s)

if x:
	print(True)
else:
	print(False)
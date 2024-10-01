# Regex and Parsing - validating and parsing email

import re

def email_val(s, name):

    exp = re.compile(r'^(?P<username>[A-Za-z]+[\w\-\.]+)@(?P<domain>[a-zA-Z]+)\.(?P<extension>[a-zA-Z]{1,3})$')
    match = exp.match(s)

    if match:
        d = match.groupdict()
        print(name.upper(), "<%s>" % match.group())


with open("./input.txt", "r") as file:

    n = int(file.readline())
    for _ in range(n):

        name, email = file.readline().split() 
        email_val(email.strip("<>"), name)



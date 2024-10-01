# Built Ins - ginortS

with open("./input.txt", "r") as file:

	s = file.readline().rstrip()


upper_list, lower_list, even_list, odd_list = [], [], [], []

for char in s:
	if char.isalpha():
		if char.islower():
			lower_list.append(char)
		else:
			upper_list.append(char)
	elif char.isdigit() and int(char) % 2 == 0:
		even_list.append(char)
	else:
		odd_list.append(char)

upper_list.sort()
lower_list.sort()
even_list.sort()
odd_list.sort()

res = [*lower_list, *upper_list, *odd_list, *even_list]

print("".join(res))
import calendar


with open("./input.txt", "r") as file:

	m, d, y = list(map(int, file.readline().split()))

	res = calendar.weekday(y, m ,d)
	print(calendar.day_name[res])



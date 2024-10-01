# Calendar - Time Delta


from datetime import datetime

with open("./input.txt", "r") as file:

	T = int(file.readline())

	for i in range(T):

		time1 = file.readline().rstrip()
		time2 = file.readline().rstrip()
		
		time_format = "%a %d %b %Y %H:%M:%S %z"

		time1 = datetime.strptime(time1, time_format)
		time2 = datetime.strptime(time2, time_format)

		delta = time1 - time2

		res = abs(int(delta.total_seconds()))
		print(res)


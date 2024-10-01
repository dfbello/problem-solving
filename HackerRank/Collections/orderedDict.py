# Collections - OrderedDict()

from collections import OrderedDict


od = OrderedDict()

with open("./input.txt", "r") as file:
	N = int(file.readline())

	items_bought = []
	for i in range(N):
		item, price = file.readline().rsplit(maxsplit=1)
		price = int(price)

		if item in od:
			od[item] += price
		else:
			od[item] = price	

for x, y in od.items():

	print(x , y)


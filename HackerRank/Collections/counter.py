# Collections -  counter()

from collections import Counter

def sell_shoe(st, size, price):
	if st[size] > 0:
		st.subtract([size])
		return price
	else:
		return 0



with open("./input.txt", "r") as file:

	_ = file.readline()
	shoes = list(map(int, file.readline().split()))
	
	stock = Counter(shoes)
	cash = 0

	N = int(file.readline())
	for i in range(N):
		size, price = list(map(int, file.readline().split()))
		cash += sell_shoe(stock, size, price)

print(cash)

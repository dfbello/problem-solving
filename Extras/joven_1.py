# Prueba proporcionada por el joven - 19/08/2024

def isAlienSorted(words, order, index=0):


	for i in range(len(words) - 1):

		curr = words[i]
		nxt = words[i+1]
		if order.find(curr[index]) > order.find(nxt[index]):
			return False
		if order.find(curr[index]) == order.find(nxt[index]):

			if len(nxt) <= index + 1 or len(curr) <= index + 1:
				if len(curr) <= len(nxt):
					continue
				else:
					return False

			if not isAlienSorted([curr, nxt], order, index + 1):
				return False


	return True





with open("./input.txt", "r") as file:

	words = file.readline().split()
	order = file.readline()

print(isAlienSorted(words, order))
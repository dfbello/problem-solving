
def maxProfit(prices):
	
	cheapest = 10 **4 + 1
	profit = 0

	for price in prices:

		if price < cheapest:
			cheapest = price
			continue

		curr = price - cheapest	
		if curr > profit:
			profit = curr
		
		

	return profit



price = [7,1,5,3,6,4]
print(maxProfit(price))
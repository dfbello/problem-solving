def intervalIntersections(firstList, secondList):
	nf = len(firstList)
	ns = len(secondList)
	n = min(nf, ns)

	res = []

	for i in range(n):
		a,b = firstList[i]
		c,d = secondList[i]

		res.append([max(a,c), min(b,d)])

	return res

f = [[0,2],[5,10],[13,23],[24,25]]
s = [[1,5],[8,12],[15,24],[25,26]]


print(intervalIntersections(f,s))
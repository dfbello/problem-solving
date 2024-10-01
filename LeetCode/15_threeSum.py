def threeSum(nums):
	l,r,m = 0, len(nums) -1 , 1

	od = sorted(nums)
	res = set()
	
	while m < len(nums) - 1:
		while l < m and m < r:
			suma = od[l] + od[m] + od[r]
			if suma == 0:
				res.add((od[l],od[m],od[r]))
				l += 1
				r -= 1
				continue
			elif suma > 0:
				r -= 1
				continue
			elif suma < 0:
				l += 1
				continue
			
		l = 0
		r = len(nums) -1		
		m += 1

	return [list(x) for x in res]




nums = [3,0,-2,-1,1,2]
print(threeSum(nums))

def sortedSquares(nums):

	i = 0
	while nums[i] < 0 and i < len(nums) - 1:
		i += 1

	if i == 0:
		return [x**2 for x in nums]

	l = i - 1
	r = i
		
	res = []
	while l >= 0 and r < len(nums):
		if nums[l]**2 < nums[r]**2:
			res.append(nums[l]**2)
			l -= 1
		else:
			res.append(nums[r]**2)
			r += 1
	
	if l >= 0:
		res.extend([x**2 for x in nums[l::-1]])
	if r < len(nums):
		res.extend([x**2 for x in nums[r:]])

	return res


nums = [-13,-11,-7,-5, -4, -1]
print(sortedSquares(nums))

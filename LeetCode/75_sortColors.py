def sortColors(nums):

	rwb = [0,0,0]

	for x in nums:
		rwb[x] += 1
	
	j = 0
	for k in range(3):
		for i in range(rwb[k]):
			nums[j] = k
			j += 1





nums = [1,1,0,1]
sortColors(nums)
print(nums)
def moveZeroes(nums):
	z, i = 0, 1
	n = len(nums)
 
	while z < n - 1 and i < n:
		print(nums)
		if nums[i] == 0:
			i += 1
			continue
		if nums[z] != 0:
			z += 1
			continue
		if z > i:
			i = z + 1
			continue

		nums[z] = nums[i]
		nums[i] = 0




nums = [4,2,4,0,0,3,0,5,1,0]
moveZeroes(nums)
print(nums)


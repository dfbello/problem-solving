def rotate(nums, k):
	k = k % len(nums)

	nums.reverse()

	l, r = 0, k - 1
	while l < r:
		nums[l], nums[r] = nums[r], nums[l]
		l +=1
		r -=1

	l, r = k, len(nums) -1
	while l < r:
		nums[l], nums[r] = nums[r], nums[l]
		l +=1
		r -=1










nums = [1,2,3]

rotate(nums, 4)
print(nums)
def removeElement(nums, val):

	l,r = 0, len(nums) -1
	k = len(nums)
	vals = 0

	while l <= r:

		if nums[l] == val and nums[r] != val:

			nums[l] = nums[r]
			k -= 1
			l += 1
			r -= 1

		if nums[l] != val:
			l += 1
		if nums[r] == val:
			r-= 1
			k -= 1
			vals += 1 

	print("swaps: %d | k: %d | %s" % (vals, k, nums))

	if vals == len(nums):
		return 0

	return k


n = [5,5]
val = 5
print(removeElement(n, val))
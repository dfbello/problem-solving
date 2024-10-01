def containsDuplicate(nums):

	n = len(nums)
	k = len(set(nums))

	return not (n == k)



nums = [1,2,3,1]
print(containsDuplicate(nums))
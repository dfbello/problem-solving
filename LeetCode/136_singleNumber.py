def singleNumber(nums):
	res = 0

	for x in nums:
		res = res ^ x

	return res

nums = [3]

print(singleNumber(nums))
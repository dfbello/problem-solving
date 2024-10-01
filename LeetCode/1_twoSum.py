
def twoSum(nums, target):
	i_nums = list(enumerate(nums))
	i_nums.sort(key=lambda x: x[1])

	l = 0
	r = -1
	suma = i_nums[l][1] + i_nums[r][1]

	while suma != target:
		
		if suma < target:
			l += 1
		else:
			r -= 1

		suma = i_nums[l][1] + i_nums[r][1]







	return [i_nums[l][0], i_nums[r][0]]


nums = [-2,4,6,9,-8,16,3,3]
target = 6

print(twoSum(nums,target))


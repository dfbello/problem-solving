def minim(arr, l, r):
	if arr[l] < arr[r]:
		return l
	else:
		return r

def maxArea(height):

	l = 0
	r = len(height) - 1

	res = 0
	while l < r:
		min_ = minim(height, l, r)

		curr = height[min_] * (r - l)
		if curr > res:
			res = curr

		if min_ == l:
			l += 1
		else:
			r -= 1

	return res

nums = [1,8,6,2,5,4,8,3,7]
print(maxArea(nums))
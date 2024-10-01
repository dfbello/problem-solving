

def merge(nums1, m, nums2, n):

	if n == 0:
		pass
	elif m == 0:
		nums1.clear()
		nums1.extend(nums2)
	else:

		res = []
		insertions = 0
		index1 = 0
		index2 = 0
		while insertions < n + m:

			try:
				while nums1[index1] <= nums2[index2] and index1 < m:
					res.append(nums1[index1])
					insertions += 1
					index1 += 1
			except IndexError as e:
				while index1 < m:
					res.append(nums1[index1])
					insertions += 1
					index1 += 1
			

			while index2 < n and (nums2[index2] <= nums1[index1] or index1 == m):
				res.append(nums2[index2])
				insertions += 1
				index2 += 1
			

		nums1.clear()
		nums1.extend(res)
		print(nums1)

	

nums1 = [0,0,3,0,0,0,0,0,0]
m = 3
nums2 = [-1,1,1,1,2,3]
n = 6


merge(nums1, m, nums2, n)
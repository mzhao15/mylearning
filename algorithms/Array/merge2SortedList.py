def merge(arr1,arr2):
	n1 = len(arr1)
	n2 = len(arr2)
	res = [0 for _ in range(n1+n2)]
	i = j = k = 0
	while i<n1 and i<n2:
		if arr1[i] < arr2[j]:
			res[k] = arr1[i]
			i += 1
		else:
			res[k] = arr2[j]
			j += 1
		k += 1
	while i < n1:
		res[k] = arr1[i]
		i += 1
		k += 1
	while j < n2:
		res[k] = arr2[j]
		j += 1
		k += 1
	return res
# merge two sorted list in-place
# def merge(nums1,nums2):
# 	m = len(nums1)
# 	n = len(nums2)
# 	i = m-1
# 	j = n-1
# 	k = m+n-1
# 	while i>=0 and j>=0:
# 		if nums1[i]>nums2[j]:
# 			nums1[k] = nums1[i]
# 			i -= 1
# 		else:
# 			nums1[k] = nums2[j]
# 			j -= 1
# 		k -= 1
# 	while j>=0:
# 		nums1[k] = nums2[j]
# 		j -= 1
# 		k -= 1

arr1 = [1,3,4,7,9]
arr2 = [2,3,6,8]
print(merge(arr1,arr2))

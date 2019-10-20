def removeDuplicates(nums):
	i = 0
	for num in nums:
		if i < 2 or num > nums[i-2]:
			nums[i] = num
			i += 1
	return i


	## need to reconsider the last element. not easy!
	# if len(nums) <= 2:
	# 	return nums
	# i = 0
	# j = 0
	# while True:
	# 	count = 1
	# 	cur = nums[j]
	# 	while j < len(nums)-1 and nums[j] == nums[j+1]:
	# 		count += 1
	# 		j += 1
	# 	if j == len(nums)-2:
	# 		if nums[-1] == nums[-2]:
	# 			count += 1
	# 	j += 1
	# 	if count == 1:
	# 		nums[i] = cur
	# 		i += 1
	# 	else:
	# 		nums[i] = nums[i+1] = cur
	# 		i += 2
	# 	print("%d %d"%(i,j))
	# 	if j == len(nums)-1:
	# 		return i
	

nums = [1,1,1,2,2,3]
n = removeDuplicates(nums)
print(n)
print(nums[:n])
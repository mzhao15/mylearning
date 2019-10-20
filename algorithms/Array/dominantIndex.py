def dominantIndex(nums):

	if len(nums) == 1:
		return 0
	maxnum = max(nums)
	for num in nums:
		if num/maxnum!=1 and num/maxnum > 0.5:
			return -1
	return nums.index(maxnum)



nums = [1,2,3,4]
print(dominantIndex(nums))
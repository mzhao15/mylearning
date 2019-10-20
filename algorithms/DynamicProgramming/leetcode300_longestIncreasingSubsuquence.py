# dynamic programming
def lengthOfLIS(nums):
	if not nums:
		return
	n = len(nums)
	le = [1]*n

	for i in range(n):
		maxlej = 0
		for j in range(0,i):
			if nums[i] > nums[j]:
				maxlej = max(maxlej,le[j])
		le[i] = maxlej + 1

	return max(le)

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))
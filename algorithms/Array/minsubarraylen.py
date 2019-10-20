
def minSubArrayLen(s, nums):
	ans = float('inf')
	i = 0
	j = 0
	total = 0
	while i < len(nums):
		while j < len(nums) and total < s:
			total += nums[j]
			j += 1
		if total >= s:
			ans = min(ans, j - i)
		total -= nums[i]
		i += 1
	if ans < float('inf'):
		return ans
	else:
		return 0


s = 3
nums = [1,1]
print(minSubArrayLen(s, nums))

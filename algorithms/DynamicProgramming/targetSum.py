def targetSum(nums,S):
	nums.sort()
	n = len(nums)
	total = sum(nums)
	offset = total
	if total < S:
		return 0
	DP = [[0]*(2*total+1) for _ in range(n+1)]
	# use zero element, there is only one way to get sum = 0
	for i in range(2*total+1):
		DP[0][i] = 1
	for i in range(n):
		for j in range(nums[i],2*total+1)

nums = [1,1,1,1,1]
S = 3
print(targetSum(nums,S))
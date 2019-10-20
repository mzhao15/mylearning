def findLongestChain(pairs):
	"""
	:type pairs: List[List[int]]
	:rtype: int
	"""
	
	pairs.sort(key=lambda x:x[0])
	print(pairs)
	
	n = len(pairs)
	dp = [0]*n
	dp[0] = 1
	 
	for i in range(n):
		for j in range(i-1,-1,-1):
			if pairs[i][0]>pairs[j][1]:
				dp[i] = max(dp[i],dp[j]+1)
	print(dp)
	return dp[-1]


pairs = [[1,2], [2,3], [3,4]]
print(findLongestChain(pairs))
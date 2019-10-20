
def climb(cost):
	n = len(cost)
	dp = [0]*(n+1)
	dp[1] = cost[0]
	
	for i in range(2,n+1):
		dp[i] = min(dp[i-1],dp[i-2])+cost[i-1]
	print(dp)
	return dp[-1]

cost = [0,0,0,1]
print(climb(cost))
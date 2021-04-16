def climbStairs(n):
    # build the DP table
    if n == 1:
        return 1
    if n == 2:
        return 2

    DP = [0] * n

    DP[0] = 1
    DP[1] = 2

    for i in range(2, n):
        DP[i] = DP[i-1] + DP[i-2]

    return DP[n-1]


n = 45
print(climbStairs(n))

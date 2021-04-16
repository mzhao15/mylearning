def houseRobber(nums):
    n = len(nums)
    DP = [0] * (n+1)

    for i in range(1, n+1):
        DP[i] = max(DP[i-2] + nums[i-1], DP[i-1])
    return DP[-1]


nums = [2, 7, 9, 3, 1]
res = houseRobber(nums)
print(res)

nums = [1, 2, 3, 1]
res = houseRobber(nums)
print(res)

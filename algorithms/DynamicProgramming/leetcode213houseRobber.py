def houseRobber(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    DP = [[0 for _ in range(n + 1)] for _ in range(n)]

    nums2 = nums*2

    # i indicates starting to rob from house i
    max_money = float('-inf')
    for i in range(n):
        for j in range(1, n+1):
            if j != n:
                DP[i][j] = max(DP[i][j-2] + nums2[i+j],  DP[i][j-1])
            else:
                DP[i][j] = DP[i][j-1]

        if DP[i][-1] > max_money:
            max_money = DP[i][-1]

    return max_money


def houseRobber2(nums):
    n = len(nums)
    # if n == 1:
    #     return nums[0]

    DP = [0] * (n+1)

    # rob first one
    DP[1] = nums[0]
    for i in range(2, n+1):
        DP[i] = max(DP[i-2] + nums[i-1], DP[i-1])
    DP[n] = DP[n-1]
    print(DP)
    max_money = DP[n]

    # not rob the first one
    DP = [0] * (n+1)
    # DP[1] = 0
    for i in range(2, n+1):
        DP[i] = max(DP[i-2] + nums[i-1], DP[i-1])
    print(DP)
    return max(max_money, DP[-1])


nums = [2, 3, 2]
res = houseRobber2(nums)
print(res)

nums = [1, 2, 3, 1]
res = houseRobber2(nums)
print(res)

nums = [1]
res = houseRobber2(nums)
print(res)

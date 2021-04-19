def numSubarrayProductLessThanK1(nums, k):
    # brutal force
    ans = 0

    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums)):
            # print('current:', i, j)
            product = product * nums[j]
            if product < k:
                ans += 1
                # print(nums[i:j+1])

    return ans


def numSubarrayProductLessThanK(nums, k):

    n = len(nums)
    if len(nums) == 1 and nums[0] < k:
        return 1
    res = 0
    n = len(nums)
    j = 0
    pro = 1
    for i in range(n):
        pro *= nums[i]
        while pro >= k and j <= i:
            pro /= nums[j]
            j += 1
        res += i-j+1
    return res


nums = [10, 5, 2, 6]
k = 100
print(numSubarrayProductLessThanK(nums, k))

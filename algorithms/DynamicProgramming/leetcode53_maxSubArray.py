def maxSubArray(nums):

    max_sum = 0

    max_cur = 0

    for i in range(len(nums)):
        max_cur += nums[i]

        if max_cur < 0:
            max_cur = 0

        if max_cur > max_sum:
            max_sum = max_cur

    if max_sum == 0:
        return max(nums)

    return max_sum


nums = [-2, -2, -1, 0]
a = maxSubArray(nums)
print(a)

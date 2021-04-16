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


def maxSubArray1(nums):

    max_global = nums[0]
    max_current = nums[0]
    for i in range(1, len(nums)):
        max_current = max(nums[i], nums[i]+max_current)
        if max_current > max_global:
            max_global = max_current

    return max_global


nums = [-2, -2, -1, 0]
a = maxSubArray1(nums)
print(a)

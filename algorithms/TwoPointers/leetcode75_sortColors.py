from collections import Counter


def sortColors1(nums):
    # use Conter
    cnt = Counter(nums)

    j = 0
    for i in range(3):
        if cnt.get(i, None):
            while cnt[i] > 0:
                nums[j] = i
                cnt[i] -= 1
                j += 1
    # print(cnt)


def sortColors(nums):
    """Dutch partitioning problem, a.k.a. Dutch National Flag problem
    https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation
    """
    i, j, k = 0, 0, len(nums) - 1  # red, white, blue

    while j <= k:
        if nums[j] == 0:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
            j += 1

        elif nums[j] == 1:
            j += 1
        else:
            nums[j], nums[k] = nums[k], nums[j]
            k -= 1


nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)

nums = [2, 0, 1]
sortColors(nums)
print(nums)

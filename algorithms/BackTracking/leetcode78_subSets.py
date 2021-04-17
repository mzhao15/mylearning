
def backtrack(res, temp, nums, start):
    res.append(temp[:])

    for i in range(start, len(nums)):
        temp.append(nums[i])
        backtrack(res, temp, nums, i+1)
        temp.pop(-1)
    return


def subSets(nums):
    res = []
    temp = []
    backtrack(res, temp, nums, 0)
    return res


nums = [1, 2, 3]
print(subSets(nums))

nums = [0]
print(subSets(nums))

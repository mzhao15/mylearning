def binary_search(nums, target):

    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


a = [2, 3, 4, 10, 40, 50]
print(binary_search(a, 3))

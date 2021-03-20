"""
Merge Sort
"""


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid_ind = len(arr)//2
    left = merge_sort(arr[:mid_ind])
    right = merge_sort(arr[mid_ind:])

    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            res.append(right[j])
            j += 1
        else:
            res.append(left[i])
            i += 1
    if i == len(left):
        res.extend(right[j:])
    else:
        res.extend(left[i:])
    return res


a = [1]  # edge case 1
print(merge_sort(a))
b = []  # edge case 2
print(merge_sort(b))
c = [3, 2, 4, 1]
print(merge_sort(c))

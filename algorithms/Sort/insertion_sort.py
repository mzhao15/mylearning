"""
Insertion Sort
"""


def sort_insertion(array):
    for i in range(len(array)):
        for j in range(i, 0, -1):
            if type(array[j]) != int and type(array[j] != float):
                return j
            if array[j] > array[j-1]:
                t = array[j]
                array[j] = array[j-1]
                array[j-1] = t

    return array


def insertion_sort(arr):
    if len(arr) < 2:
        return arr
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr


def binary_insertion_sort(arr):
    if len(arr) < 2:
        return arr
    # replace the comparison by a binary search then swap. Can increase the efficiency
    return arr


a = [3, 2, 4, 1]
# a = [1]  # edge case 1
# a = []  # edge case 2
print(insertion_sort(a))

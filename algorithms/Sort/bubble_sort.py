

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)-i):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return


a = [1]  # edge case 1
bubble_sort(a)
print(a)
b = []  # edge case 2
bubble_sort(b)
print(b)
c = [3, 2, 4, 1]
bubble_sort(c)
print(c)

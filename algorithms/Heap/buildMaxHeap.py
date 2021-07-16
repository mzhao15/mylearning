def max_heapify(arr, heapsize, m):

    l = 2*m + 1
    r = 2*m + 2
    largest = m

    if l < heapsize and arr[m] < arr[l]:
        largest = l

    if r < heapsize and arr[largest] < arr[r]:
        largest = r

    if largest != m:
        arr[largest], arr[m] = arr[m], arr[largest]
        max_heapify(arr, heapsize, largest)


def buildMaxHeap(arr):

    heapsize = len(arr)
    for i in range(heapsize//2 - 1, -1, -1):
        # start from heapsize//2-1 down to root because the rest of nodes are leaves
        max_heapify(arr, heapsize, i)
    return


arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print('Original Arrary: ', arr)
buildMaxHeap(arr)
print('Heap: ', arr)

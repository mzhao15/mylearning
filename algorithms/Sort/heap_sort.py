
# Python program for implementation of heap Sort
# very similar to selection sort

# To heapify subtree rooted at index i.
# n is size of heap


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


def heapify2(arr, n, i):
    """Heapify an array

    Args:
        arr (list): list to represent the heap elements
        i (int): the key to heapfiy
        n (int): heap size
    """
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i

    if l < n and arr[l] > arr[i]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, n)
    return


def heap_sort(arr):

    n = len(arr)

    # build a max heap first
    for i in range(n//2, -1, -1):
        heapify2(arr, n, i)

    for k in range(n-1, 0, -1):
        arr[0], arr[k] = arr[k], arr[0]
        heapify2(arr, k-1, 0)
    return arr


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
n = len(arr)
print("Sorted array is %s" % arr)

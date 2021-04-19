def longestMountain(arr):

    start = 0
    maxlen = 0
    peak = False
    for i in range(len(arr)):
        if i+1 < len(arr) and i-1 >= 0 and arr[i] <= arr[i+1] and arr[i] <= arr[i-1]:
            start = i
            peak = False
        elif i-1 >= 0 and i+1 < len(arr) and arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            peak = True
        elif peak and i-1 >= 0 and arr[i] < arr[i-1]:
            maxlen = max(maxlen, i-start+1)

    return maxlen


arr = [2, 1, 4, 7, 3, 2, 5]
print(longestMountain(arr))


arr = [2, 2, 2]
print(longestMountain(arr))

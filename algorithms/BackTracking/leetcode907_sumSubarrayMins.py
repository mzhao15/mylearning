def backtrack():
    return


def sumSubarrayMins(arr):
    ans = 0

    n = len(arr)

    for i in range(n):
        for j in range(n-i):
            ans += arr[i:j]

    return


arr = [3, 1, 2, 4]
print(sumSubarrayMins(arr))

arr = [11, 81, 94, 43, 3]
print(sumSubarrayMins(arr))

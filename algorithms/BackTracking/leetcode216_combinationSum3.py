def backtrack(ans, temp, k, n, start):

    if k == 0 and n == 0:
        ans.append(temp[:])
        return
    elif n < 0:
        return

    for i in range(start, 10):
        temp.append(i)
        backtrack(ans, temp, k-1, n-i, i+1)
        temp.pop(-1)


def combinationSum3(k, n):

    ans = []
    temp = []
    backtrack(ans, temp, k, n, 1)
    return ans


k = 3
n = 7
print(combinationSum3(k, n))

k = 3
n = 9
print(combinationSum3(k, n))

k = 4
n = 1
print(combinationSum3(k, n))

k = 3
n = 2
print(combinationSum3(k, n))

k = 9
n = 45
print(combinationSum3(k, n))

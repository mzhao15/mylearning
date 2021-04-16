import math


def numSquares(n):

    DP = [i for i in range(n+1)]

    for i in range(1, n+1):
        min_num = DP[i]
        k = int(math.sqrt(i))
        for j in range(1, k+1):
            if (i - j*j) >= 0 and (DP[i-j*j] + 1 < min_num):
                min_num = DP[i-j*j] + 1
        DP[i] = min_num

    print(DP)
    return DP[-1]


n = 12
print(numSquares(n))


n = 13
print(numSquares(n))

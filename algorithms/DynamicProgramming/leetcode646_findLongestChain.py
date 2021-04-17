def findLongestChain(pairs):

    n = len(pairs)
    sorted_pairs = sorted(pairs, key=lambda x: x[0])

    DP = [0 for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(i):
            if sorted_pairs[j-1][1] < sorted_pairs[i-1][0]:
                DP[i] = max(DP[i], DP[j] + 1)

    print(DP)
    return DP[-1] + 1  # why plus 1


a = [[1, 2], [3, 4], [2, 3]]
print(findLongestChain(a))

a = [[-10, -8], [-6, -4], [-5, 0], [-4, 7], [1, 7], [6, 10], [8, 9], [9, 10]]
# print(sorted(a, key=lambda x: x[0]))
print(findLongestChain(a))

a = [[-9, 8], [-6, 9], [-6, -2], [-5, 3], [-1, 4], [0, 3], [1, 6], [8, 10]]
# print(sorted(a, key=lambda x: x[0]))
print(findLongestChain(a))


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    m = len(s)
    res = [[False for _ in range(m)] for _ in range(m)]
    for i in range(m):
        res[i][i] = True
        if i < m-1 and s[i] == s[i+1]:
            res[i][i+1] = True
    for i in range(m-1, -1, -1):
        for j in range(i+2, m):
            if res[i+1][j-1] == True and s[i] == s[j]:
                res[i][j] = True
            else:
                res[i][j] = False
    for result in res:
        print(result)
    maxlen = float('-inf')
    start = 0
    end = m-1
    for i in range(m):
        for j in range(i, m):
            if res[i][j] == True and j-i+1 > maxlen:
                maxlen = j-i+1
                start = i
                end = j
            # print(s[start:end+1])
    return s[start:end+1]


def longestPalindrome2(s):
    n = len(s)
    DP = [[False for _ in range(n)] for _ in range(n)]
    print(*DP, sep='\n')
    print('\n')

    # base cases
    for i in range(n):
        DP[i][i] = True
        # print(i)
        # print(*DP, sep='\n')
        # print('\n')
        if (i + 1 < n) and (s[i] == s[i+1]):
            DP[i][i+1] = True
            print('yes')
    print(*DP, sep='\n')
    print('\n')

    # increasse substring length
    k = 3
    while k <= n:
        for i in range(n-k+1):
            j = i + k - 1
            DP[i][j] = DP[i+1][j-1] and (s[i] == s[j])
        k += 1

    maxlen = float('-inf')
    print(*DP, sep='\n')

    for i in range(n):
        for j in range(i, n):
            if DP[i][j] and maxlen < j - i + 1:
                maxlen = j - i + 1
                res = s[i:j]
    return res


s = 'abcba'
print(longestPalindrome2(s))

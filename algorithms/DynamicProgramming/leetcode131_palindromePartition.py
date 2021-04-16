
def ispalindraome1(s):
    return s == s[::-1]


def ispalindraome(s):
    if len(s) == 1:
        return True

    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            return False

    return True


def palindromePartition1(s):
    res = []

    n = len(s)

    DP = [[] for _ in range(n)]

    for i in range(n):
        for j in range(0, n):
            if i+j < n and ispalindraome(s[i:i+j+1]):
                DP[i].append(s[i:i+j+1])
    return res


def dfs(s, path, res):

    if not s:
        res.append(path)
        return
    for i in range(1, len(s)+1):
        if ispalindraome(s[:i]):
            dfs(s[i:], path+[s[:i]], res)
    return


def palindromePartition(s):
    res = []
    dfs(s, [], res)
    return res


# print(ispalindraome('a'))


# s = 'aab'
# res = palindromePartition1(s)
# print(*res, sep='\n')

s = 'aab'
res = palindromePartition(s)
print(*res, sep='\n')

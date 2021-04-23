def numDecodings(s):
    if not s or s[0] == '0':
        return 0

    DP = [0 for i in range(len(s)+1)]

    DP[0:2] = [1, 1]

    for i in range(2, len(s) + 1):
        if 0 < int(s[i-1:i]) <= 9:
            DP[i] += DP[i-1]
        if 10 <= int(s[i-2:i]) <= 26:
            DP[i] += DP[i-2]
    return DP[-1]


s = '12'
print(numDecodings(s))

s = '226'
print(numDecodings(s))

s = '0'
print(numDecodings(s))

s = "06"
print(numDecodings(s))

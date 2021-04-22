def lengthOfLastWord(s):

    ans = 0
    i = len(s)-1

    while i >= 0 and s[i] == ' ':
        i -= 1
    # print(i, s[i])
    if i < 0:
        return 0
    else:
        for j in range(i, -1, -1):
            if s[j] != ' ':
                ans += 1
            else:
                return ans
    return ans


s = "Hello World"
print(lengthOfLastWord(s))

s = " "
print(lengthOfLastWord(s))

s = "a "
print(lengthOfLastWord(s))

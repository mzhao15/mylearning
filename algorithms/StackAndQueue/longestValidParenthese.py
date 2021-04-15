def longestValidParentheses(s):
    maxlen = 0
    stack = list(s)
    curlen = 0
    for i in range(len(s)-1, -1, -1):
        right = stack.pop()
        if right == ')' and i-1 >= 0 and s[-1] == '(':
            curlen += 2
            s
    return maxlen


s = "(()"
print(longestValidParentheses(s))

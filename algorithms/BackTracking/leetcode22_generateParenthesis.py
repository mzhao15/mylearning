def generateParenthesis(n):

    ans = []
    temp = ''

    def helper(ans, temp, left, right):
        if left == n and right == n:
            ans.append(temp)

        if left < n:
            helper(ans, temp + '(', left+1, right)
        if right < left:
            helper(ans, temp + ')', left, right+1)

    helper(ans, temp, 0, 0)
    return ans


n = 3
print(generateParenthesis(n))

n = 1
print(generateParenthesis(n))

def letterCombinations(digits):
    # phone = {}
    # start = 'a'
    # for i in range(2, 10):
    #     phone[str(i)] = [chr(ord(start) + j) for j in range(3)]
    #     start = chr(ord(phone[str(i)][2]) + 1)
    #     print(start)
    # print(phone)
    phone = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    n = len(digits)
    ans = []
    temp = []

    if n == 0:
        return ans

    def helper(ans, temp, digits):
        if len(digits) == 0 and len(temp) == n:
            ans.append(''.join(temp[:]))

        for i, digit in enumerate(digits):
            for letter in phone[digit]:
                temp.append(letter)
                helper(ans, temp, digits[i+1:])
                temp.pop()
        return

    helper(ans, temp, digits)
    return ans


digits = "23"
print(letterCombinations(digits))

digits = ""
print(letterCombinations(digits))

digits = "2"
print(letterCombinations(digits))

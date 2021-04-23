def reverseWord(word):
    word = list(word)
    i = 0
    j = len(word) - 1
    while i < j:
        word[i], word[j] = word[j], word[i]
        i += 1
        j -= 1
    return ''.join(word)


def reverseWords(s):
    s = reverseWord(s)
    words = [w for w in s.strip().split(' ') if w]
    return ' '.join([reverseWord(word) for word in words])


s = "the sky is blue"
print(reverseWords(s))

s = "  hello world  "
print(reverseWords(s))

s = "a good   example"
print(reverseWords(s))

s = "  Bob    Loves  Alice  "
print(reverseWords(s))

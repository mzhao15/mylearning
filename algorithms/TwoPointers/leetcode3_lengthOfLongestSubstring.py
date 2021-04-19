# this is almost the same as leetcode 904


def lengthOfLongestSubstring2(s):

    visited = {}
    maxlen = 0
    start = 0   # starting index of the substring
    for i, ch in enumerate(s):
        if ch in visited and start <= visited[ch]:
            start = visited[ch] + 1
        else:
            maxlen = max(maxlen, i - start + 1)
        visited[ch] = i

    return maxlen


def lengthOfLongestSubstring(s):
    # use two pointers
    n = len(s)
    if n <= 1:
        return n

    i = 0
    j = 1
    substr = [s[0]]
    maxlen = 1
    while j < n:
        ch = s[j]
        if s[j] not in substr:
            maxlen = max(maxlen, j - i + 1)
        else:
            while 1:  # this step can be improved by using a hashbable which records the first previous index of this char.
                i += 1
                if substr.pop(0) == ch:
                    break

        substr.append(ch)
        j += 1
        # print(substr)

    return maxlen


s = 'abcabcbb'
print(lengthOfLongestSubstring2(s))


s = 'bbbbb'
print(lengthOfLongestSubstring2(s))


s = 'pwwkew'
print(lengthOfLongestSubstring2(s))


s = ''
print(lengthOfLongestSubstring2(s))

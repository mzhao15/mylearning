
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
	for i in range(m-1,-1,-1):
		for j in range(i+2,m):
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
		for j in range(i,m):
			if res[i][j] == True and j-i+1 > maxlen:
				maxlen = j-i+1
				start = i
				end = j
			# print(s[start:end+1])
	return s[start:end+1]


s = 'abcba'
print(longestPalindrome(s))
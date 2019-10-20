def wordBreak(s, wordDict):
	"""
	:type s: str
	:type wordDict: List[str]
	:rtype: bool
	"""
	"Dynamic Programming"
	if not s or not wordDict:
		return False
	res = [False]*(len(s)+1)
	res[0] = True
	for i in range(1,len(s)+1):
		for j in range(i,-1,-1):
			sub = s[i-j:i]
			if sub in wordDict:
				if res[i-j] == True:
					res[i] = True
					break
	return res[-1]

s = 'leetcode'
wordDict = ['leet','code']
print(wordBreak(s,wordDict))  
	

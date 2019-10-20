
from collections import Counter
def wordSubsets(A,B):
	dic = {}
	for word in B:
		temp = Counter(word)
		for ch in temp:
			if ch not in dic:
				dic[ch] = temp[ch]
			elif temp[ch] > dic[ch]:
				dic[ch] = temp[ch]
	res = []
	for word in A:
		temp = Counter(word)
		flag = True
		for ch in dic:
			if temp[ch] < dic[ch]:
				flag = False
		if flag:
			res.append(word)
	return res

A = ["amazon","apple","facebook","google","leetcode"]
B = ["lo","eo"]
print(wordSubsets(A,B))

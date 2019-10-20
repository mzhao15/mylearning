
words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"

find = []
for word in words:
	dic = {}
	isfind = 1
	for i,letter in enumerate(pattern):
		if letter not in dic.keys():
			if word[i] not in dic.values():
				dic[letter] = word[i]
			else:
				isfind = 0
				break
		elif dic[letter] != word[i]:
			isfind = 0
			break
	if isfind == 1:
		find.append(word)
print(find)



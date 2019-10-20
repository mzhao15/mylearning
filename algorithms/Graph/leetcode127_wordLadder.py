def ladderLength(beginWord, endWord, wordList):
	# build a hash table: key is word in wordlist, val is a list which key can transform to
	graph = buildmap(wordList,beginWord)
	print(graph)
	# bfs
	queue = [beginWord]
	used = set(beginWord)
	step = 1
	while queue:
		for _ in range(len(queue)):
			cur = queue.pop(0)
			if cur == endWord: return step
			for word in graph[cur]:
				if word not in used:
					used.add(word)
					queue.append(word)
		step += 1
	return 0

def buildmap(wordList,beginWord):
	# graph = {word:[] for word in wordList}
	graph = {word:set() for word in wordList}
	for word in wordList:
		worddiff(word,graph,wordList)
	if beginWord not in wordList:
		graph[beginWord] = set()
		worddiff(beginWord,graph,wordList)		
	return graph

def worddiff(word,graph,wordList):
	for i in range(len(word)):
		cur = word[i]
		for ch in 'abcdefghijklmnopqrstuvwxyz':
			if cur!=ch:
				newword = word[:i]+ch+word[i+1:]
				if newword in wordList:
					graph[word].add(newword)


# def buildmap(wordList,beginWord):
# 	# graph = {word:[] for word in wordList}
# 	graph = {word:set() for word in wordList}
# 	graph[beginWord] = set()
# 	for word1 in wordList:
# 		for word2 in wordList:
# 			if word1!=word2 and worddiff(word1,word2):
# 				graph[word1].append(word2)
# 	if beginWord not in wordList:
# 		for word in wordList:
# 			if worddiff(beginWord,word):
# 				graph[beginWord].append(word)
# 	return graph

# def worddiff(word1,word2):
# 	cnt = 0
# 	for i,ch in enumerate(word1):
# 		if ch == word2[i]:
# 			cnt += 1
# 	if cnt == len(word1)-1:
# 		return True
# 	else:
# 		return False


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLength(beginWord,endWord,wordList))



def construct_dict(wordList):
	d = {}
	for word in wordList:
		for i in range(len(word)):
			s = word[:i] + "_" + word[i+1:]
			d[s] = d.get(s, []) + [word]
	return d
# print(construct_dict(wordList))
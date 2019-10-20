def groupAnagrams(strs):
	temp = {}
	for string in strs:
		sorted_str = ''.join(sorted(list(string)))
		if sorted_str not in temp:
			temp[sorted_str] = [string]
		else:
			temp[sorted_str].append(string)
	res = []
	for value in temp.values():
		res.append(value)
	return res
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
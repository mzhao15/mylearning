def groupAnagrams(strs):
    from collections import defaultdict

    dic = defaultdict(list)
    for s in strs:
        ss = ''.join(sorted(s))
        dic[ss].append(s)

    return list(dic.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))


strs = [""]
print(groupAnagrams(strs))

strs = ["a"]
print(groupAnagrams(strs))

def search(s):
	if not s:
		return
	counts = {}
	indices = {} 
	for i,ch in enumerate(s):
		if ch not in counts:
			counts[ch] = 1
			indices[ch] = [i]
		else:
			counts[ch] += 1
			indices[ch].append(i)
	for ch in counts.keys():
		if counts[ch] == 1:
			break
	return indices[ch]

s = 'ababd'
print(search(s))

	

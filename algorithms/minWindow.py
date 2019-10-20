import sys

def minWindow(S,T):
	if not S or not T:
		return ""
	lens = len(S)
	lent = len(T)
	if lens < lent:
		return ""
	
	l = r = 0
	head = 0
	counter = {}
	for c in T:
		if c not in counter:
			counter[c] = 1
		else:
			counter[c] += 1
	templen = lent
	minlen = sys.maxsize
	while r < lens:
		if counter[S[r]] > 0:
			templen -= 1 
		counter[S[r]] -= 1
		r += 1
		while templen == 0:
			if r-l < minlen:
				minlen = r-l
				head = l
			counter[S[l]] += 1
			if counter[S[l]] > 0:
				templen += 1

			l += 1
	
	if minlen == sys.maxsize:
		return ""
	else:
		return S[head:head+minlen]
	



def getindex(ch,T):
	for i,letter in enumerate(T):
		if ch == letter:
			return i
	return -1




S = "ADOBECODEBANC"
T = "ABC"
print(minWindow(S,T))
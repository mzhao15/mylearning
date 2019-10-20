def cipher(k, s):
	n = len(s)+1-k
	res = ''
	res += s[0]
	for i in range(1,k+1):
		res += str(int(s[i])^int(s[i-1]))
	m = 0
	for j in range(k+1,n):
		res += str(int(s[j])^int(s[j-1])^int(res[m]))
		m += 1
	return res


k = 4
s = '1110101001'
print(cipher(k,s))
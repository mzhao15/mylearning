def PascalTriangles(k):
	res = [[0 for _ in range(i+1)] for i in range(k)]

	for i in range(k):
		res[i][0] = 1
		res[i][-1] = 1
		for j in range(1,i):
			res[i][j] = res[i-1][j-1] + res[i-1][j]
	return res

k = 7
ans = PascalTriangles(k)
for i in range(k):
	print(ans[i])
def combinations(n,k):
	results = []
	temp = []
	if n <= 0 or k <= 0: return results
	combinationshelper(n,k,1,results,temp)
	return results
def combinationshelper(n,k,st_num,results,temp):
	if k == 0:
		results.append(temp[:])
	else:
		for i in range(st_num,n+1):
			temp.append(i)
			combinationshelper(n,k-1,i+1,results,temp)
			temp.pop()


n = 4
k = 2
print(combinations(n,k))


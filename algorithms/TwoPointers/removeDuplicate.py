def removeDuplicate(A):
	if len(A)<2:
		return
	j = 0
	for i in range(1,len(A)):
		if A[i] != A[j]:
			j += 1
			A[j] = A[i]
	return j+1


A = [1,1,2,3,3,4]
removeDuplicate(A)
print(A)
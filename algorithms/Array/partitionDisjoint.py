

def partitionDisjoint(A):
	i = 1
	while True:
		left = A[:i]
		right = A[i:]
		if max(left) > min(right):
			i += right.index(min(right)) + 1
			print(left)
			print(right)
		else:
			return i


A = [5,0,3,8,6]
print(partitionDisjoint(A))
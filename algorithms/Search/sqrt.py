def sqrt(A):

	left = 1
	right = A
	while left <=  right:
		mid = (left+right)//2
		if mid*mid == A:
			return mid
		elif mid*mid < A:
			left = mid+1
		else:
			right = mid-1
		print("%d %d"%(left, right))
	return left-1

print(sqrt(15))

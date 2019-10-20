def nextGreaterElements(nums):
	if not nums:
		return []
	if len(nums) == 1:
		return [-1]
	res = []
	for j,num in enumerate(nums):
		stack = []
		for i in range(j-1,-1,-1):
			stack.append(nums[i])
		for i in range(len(nums)-1,j,-1):
			stack.append(nums[i])
		# print(stack)
		while stack:
			top = stack.pop()
			if top > num:
				res.append(top)
				break
		if not stack and top <= num:
			res.append(-1)
	return res

nums = [1,1,1,1,1]
print(nextGreaterElements(nums))
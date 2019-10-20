def pivotIndex(nums):
	if len(nums) == 0:
		return -1
	if len(nums) == 1:
		return 0
	left = 0
	right = sum(nums[1:])
	i = 0
	while i < len(nums)-1 and left!=right:
		left += nums[i]
		right -= nums[i+1]
		i += 1
		print('left right %d %d'%(left,right))
	if left==right:
		return i
	return -1


nums = [1, 2, 3]
print(pivotIndex(nums))
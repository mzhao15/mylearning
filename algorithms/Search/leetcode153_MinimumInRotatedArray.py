
def findMin(nums):
	if len(nums) == 1: return nums[0]
	if nums[0]<nums[-1]: return nums[0]

	left, right = 0, len(nums)-1
	# while left <= right:
	# 	mid = left +(right-left)//2
	# 	print('%d %d %d'%(nums[left],nums[mid],nums[right]))
	# 	if nums[mid]>nums[mid+1]:
	# 		return nums[mid+1]
	# 	if nums[mid]<nums[mid-1]:
	# 		return nums[mid]
	# 	if nums[mid]>nums[0]:
	# 		left = mid+1
	# 	else:
	# 		right = mid-1
	while left<right:
		mid = left + (right-left)//2
		if nums[mid]<nums[right]:
			right = mid
		else:
			left = mid+1
	return nums[left]

nums = [4,5,6,7,0,1,2]
print(findMin(nums))


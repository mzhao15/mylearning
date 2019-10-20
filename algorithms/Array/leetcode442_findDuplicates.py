
def findDuplicates(nums):
	ans = []
	for i, num in enumerate(nums):
		if nums[abs(num)-1] > 0:
			nums[abs(num)-1] = -nums[abs(num)-1](num)
		else:
			ans.append(abs(num))
	return ans


nums = [4,3,2,7,8,2,3,1]
print(findDuplicates(nums))
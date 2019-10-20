def permute(nums):
	"""
	:type nums: List[int]
	:rtype: List[List[int]]
	"""
	results = []
	temp = []
	if not nums:
		return results
	permutehelper(nums,0,results,temp)
	return results
	
def permutehelper(nums,st_num,results,temp):
	if len(temp) == len(nums):
		results.append(temp[:])
	else:
		for i in range(len(nums)):
			if nums[i] in temp:
				continue
			temp.append(nums[i])
			permutehelper(nums,i+1,results,temp)
			temp.pop()


nums = [1,2,3]
print(permute(nums))

			
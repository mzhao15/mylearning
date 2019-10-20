
nums = [3,1,3,4,2]

def findduplicate1(nums):
	nums.sort()
	for i in range(len(nums)-1):
		if nums[i] == nums[i+1]:
			return nums[i]


def findduplicate2(nums):
	seen = set()
	for num in nums:
		if num in seen:
			return num
		else:
			seen.add(num)


print(findduplicate2(nums))
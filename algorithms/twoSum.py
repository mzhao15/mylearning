# time complexity: O(n2)
# space complexity: O(1)
nums = [2, 7, 11, 15]
target = 13

for i,num in enumerate(nums):
	k = i + 1
	for new_num in nums[i+1:]:
		if nums[i] + nums[k] == target:
			print(i,k)
		k += 1

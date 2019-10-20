def threeSum(nums):
	nums.sort()
	n = len(nums)
	ans = []
	for i in range(n-2):
		l = i+1
		r = n-1
		while l < r:
			if nums[i] + nums[l] + nums[r] == 0:
				if [nums[i],nums[l],nums[r]] not in ans:
					ans.append([nums[i],nums[l],nums[r]])
				l += 1
				r -= 1
			elif nums[i] + nums[l] + nums[r] < 0:
				l += 1
			else:
				r -= 1
	return ans


def threeSum2(nums):
	nums.sort()
	n = len(nums)
	ans = []
	for i in range(n-2):
		k = i+2
		for j in range(i+1,n-1):
			while k<n and nums[i]+nums[j]+nums[k]<0:
				print('%d %d %d'%(nums[i],nums[j],nums[k]))
				k += 1
			if k<n and nums[i]+nums[j]+nums[k]==0:
				if [nums[i],nums[j],nums[k]] not in ans:
					ans.append([nums[i],nums[j],nums[k]])
				k += 1
	return ans


nums = [1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3]
print(threeSum2(nums))
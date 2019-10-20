def largestNumber(nums):
	temp = []
	for num in nums:
		temp.extend(list(str(num)))
	temp.sort(reverse=True)
	print(temp)
	return ''.join(temp)


nums = [3,30,34,5,9]
print(largestNumber(nums))
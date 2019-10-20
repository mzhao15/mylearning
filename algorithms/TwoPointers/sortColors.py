def sortColors(nums):
	# i,j = 0,0
	# for k in range(len(nums)):
	# 	v = nums[k]
	# 	nums[k] = 2
	# 	if v<2:
	# 		nums[j] = 1
	# 		j += 1
	# 	if v==0:
	# 		nums[i] = 0
	# 		i += 1
	# 	print(nums)
		
	red, white, blue = 0, 0, len(nums)-1
	while white <= blue:
		if nums[white] == 0:
			nums[red], nums[white] = nums[white], nums[red]
			white += 1
			red += 1
		elif nums[white] == 1:
			white += 1
		else:
			nums[white], nums[blue] = nums[blue], nums[white]
			blue -= 1

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)
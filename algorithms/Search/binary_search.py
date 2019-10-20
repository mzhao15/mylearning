

def binary_search(arr,x):
	"""find x in a sorted array """
	right = len(arr)-1
	left = 0
	while left <= right:
		mid = (left + right)//2
		if arr[mid] == x:
			return mid
		elif arr[mid] < x:
			left = mid + 1
		else:
			right = mid - 1
	return -1


a = [2, 3, 4, 10, 40, 50]
print(binary_search(a,3))



		

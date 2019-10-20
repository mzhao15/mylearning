

def binary_search(array,x):
	"""find x in a sorted array """
	num = len(array)
	left = 0
	right = num-1
	while left<=right:
		mid = (left+right)//2
		#print('left:{},mid:{},right:{}'.format(left,mid,right))
		if array[mid] == x:
			return mid
		elif array[mid] < x:
			left = mid+1
		else:
			right = mid-1

		


array = [1,2,3,4,5,6,7]
ch = 5
id = binary_search(array,ch)
print(id)
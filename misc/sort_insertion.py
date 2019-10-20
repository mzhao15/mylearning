


def sort_insertion(array):
	for i in range(len(array)):
		for j in range(i,0,-1):
			if type(array[j])!=int and type(array[j]!=float):
				return j
			if array[j]>array[j-1]:
				t = array[j]
				array[j] = array[j-1]
				array[j-1] = t

	return array


a = [13,3,8,-10,0,4,7,11]
sorted_array = sort_insertion(a)
if type(sorted_array)==int:
	print('invalid item: {}'.format(sorted_array))
else:
	print(sorted_array)





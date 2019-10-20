


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







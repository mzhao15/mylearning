

def partition1(array,low,high):
	''' use the first element as pivot '''
	key = array[low]
	while low < high:
		while low < high and array[high] >= key:
			high -= 1
		while low < high and array[high] < key:
			array[low] = array[high]
			low += 1
			array[high] = array[low]
	array[low] = key
	return low

def quick_sort1(array,low,high):
    if low < high:
        key_index = partition1(array,low,high)
        quick_sort1(array,low,key_index-1)
        quick_sort1(array,key_index+1,high)

if __name__ == '__main__':
    array1 = [8,10,9,6,4,16,5,13,26,18,2,45,34,23,1,7,3]
    # array1 = []

    print(array1)
    quick_sort1(array1,0,len(array1)-1)
    print(array1)



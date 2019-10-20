
# method 3: use a heap
def mergekSortedArray(arr):
	heap = []
	cnt = 0
	for i in range(len(arr)):
		cnt += len(arr[i])
		heap.append((arr[i][0],i))
		arr[i].pop(0)
	buildheap(heap)
	res = []
	for i in range(cnt):
		res.append(heap[0][0])
		if arr[heap[0][1]]:
			heap[0] = (arr[heap[0][1]].pop(0),heap[0][1])
		else:
			heap[0] = (float('inf'),heap[0][1])
		heapify(heap,len(arr),0)
	return res


def heapify(arr,n,i):
	l = 2*i+1
	r = 2*i+2
	largest = i
	if l<n and arr[i][0] > arr[l][0] :
		largest = l
	if r<n and arr[largest][0] > arr[r][0]:
		largest = r
	if largest!=i:
		arr[largest],arr[i] = arr[i],arr[largest]
		heapify(arr,n,largest)


def buildheap(arr):
	n = len(arr)
	for i in range(len(arr)//2-1,-1,-1):
		heapify(arr,n,i)


# method 2
# def mergekSortedArray(arr):
# 	res = []
# 	for i in range(len(arr)):
# 		res.extend(arr[i])
# 	res.sort()
# 	return res


# method 1
# def mergekSortedArray(arr):
# 	m = len(arr)
# 	temp = arr
# 	while m > 1:
# 		res = []
# 		for i in range(0,m,2):
# 			if m%2!=0 and i == m-1:
# 				res.append(temp[i])
# 			else:
# 				res.append(merge2SortedArray(temp[i],temp[i+1]))
# 		m = len(res)
# 		temp = res
# 	return res[0]

# def merge2SortedArray(arr1,arr2):
# 	n1 = len(arr1)
# 	n2 = len(arr2)
# 	res = [0 for _ in range(n1+n2)]
# 	i = j = k = 0
# 	while i<n1 and i<n2:
# 		if arr1[i] < arr2[j]:
# 			res[k] = arr1[i]
# 			i += 1
# 		else:
# 			res[k] = arr2[j]
# 			j += 1
# 		k += 1
# 	while i < n1:
# 		res[k] = arr1[i]
# 		i += 1
# 		k += 1
# 	while j < n2:
# 		res[k] = arr2[j]
# 		j += 1
# 		k += 1
# 	return res

arr = [[1,4,7],[2,5,9],[1,3,9,10],[4,7,8,11],[5,10,14,16]]
print(mergekSortedArray(arr))
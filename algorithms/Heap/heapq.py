import heapq


arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print('original array: ', arr)

heapq.heapify(arr)
print('heap array: ', arr)

k = 3
bigs = heapq.nlargest(k, arr)
print(f'{k} largest elements: ', bigs)
print('current heap: ', arr)

ele = 5
heapq.heappush(arr, ele)
print(f'add one element {ele} to the heap')
print('current heap: ', arr)

print('\n')
arr2 = [(2, 1, 0), (0, 2, 0), (1, 3, 0)]
heapq.heapify(arr2)
print('heap with tuples: ', arr2)

a = heapq.heappop(arr2)
print('popped element from the heap: ', a)
print('heap after popping', arr2)


# heapq.heapreaplace()
# nlargest(k, iterable, key = fun) :- This function is used to return the k largest elements from the iterable specified and satisfying the key if mentioned.
# nsmallest(k, iterable, key = fun) :- This function is used to return the k smallest elements from the iterable specified and satisfying the key if mentioned.

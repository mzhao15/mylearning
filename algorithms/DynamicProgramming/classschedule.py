def canFinish(numCourses, prerequisites):
	"""
	:type numCourses: int
	:type prerequisites: List[List[int]]
	:rtype: bool
	"""
	# pair [0, 1]  

	indegree = [0]*numCourses
	follow = {}
	for pair in prerequisites:
		indegree[pair[0]] += 1
		if pair[1] not in follow:
			follow[pair[1]] = [pair[0],]
		else:
			follow[pair[1]].append(pair[0])
	print(indegree)
	print(follow)
	queue = []
	for i in range(numCourses):
		if indegree[i] == 0:
			queue.append(i)
	print(queue)
	while queue:
		n = queue.pop(0)
		if n in follow:
			for follower in follow[n]:
				indegree[follower] -= 1
				if indegree[follower] == 0:
					queue.append(follower)

	for i in indegree:
		if i != 0:
			return 0
	return 1



print(canFinish(2, [[1,0]]))
# leetcode 207
def canFinish(numCourses, prerequisites):
	graph = [[] for _ in range(numCourses)]
	indegree = [0]*numCourses
	for pre in prerequisites:
		graph[pre[0]].append(pre[1])
		indegree[pre[1]] += 1
	print(graph)
	print(indegree)
	queue = []
	for i in range(numCourses):
		if indegree[i] == 0:
			queue.append(i)
	while queue:
		course = queue.pop(0)
		for nextcourse in graph[course]:
			indegree[nextcourse] -= 1
			if indegree[nextcourse] == 0:
				queue.append(nextcourse)
	for i in range(numCourses):
		if indegree[i]!=0:
			return False
	return True

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(canFinish(numCourses,prerequisites))

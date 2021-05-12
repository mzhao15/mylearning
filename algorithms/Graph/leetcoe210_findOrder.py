# leetcode 210


def findOrder1(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    indegree = [0]*numCourses
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
        indegree[pre[0]] += 1
    # print(graph)
    # print(indegree)
    visited = [False]*numCourses
    queue1 = []
    queue2 = []
    for i in range(numCourses):
        if indegree[i] == 0:
            queue1.append(i)
    while queue1:
        course = queue1.pop()
        queue2.append(course)
        for nextcourse in graph[course]:
            indegree[nextcourse] -= 1
            if indegree[nextcourse] == 0:
                queue1.append(nextcourse)
    for i in range(numCourses):
        if indegree[i] != 0:
            return []
    return queue2


def findOrder2(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    indegree = [0]*numCourses
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
        indegree[pre[0]] += 1
    visited = [False]*numCourses
    recstack = [False]*numCourses
    stack = []
    for i in range(numCourses):
        if visited[i] == False:
            if not DFS(i, stack, graph, visited, recstack):
                return []
    return stack


def DFS(v, stack, graph, visited, recstack):
    visited[v] = True
    recstack[v] = True
    flag = True
    for ver in graph[v]:
        if visited[ver] == False:
            flag = DFS(ver, stack, graph, visited, recstack)
        elif recstack[ver] == True:
            return False
    stack.insert(0, v)
    recstack[v] = False
    if flag == False:
        return False
    else:
        return True


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [1, 3]]
print(findOrder1(numCourses, prerequisites))
print(findOrder2(numCourses, prerequisites))

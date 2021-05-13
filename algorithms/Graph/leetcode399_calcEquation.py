from collections import defaultdict


def calcEquation(equations, values, queries):
    def helper(eqs, vals, qry):
        graph = defaultdict(list)
        for eq in eqs:
            graph[eq[0]].append(eq[1])

        print(graph)

        return 0

    return [helper(equations, values, query) for query in queries]


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(calcEquation(equations, values, queries))

# equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
# values = [1.5, 2.5, 5.0]
# queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
# print(calcEquation(equations, values, queries))

# equations = [["a", "b"]]
# values = [0.5]
# queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
# print(calcEquation(equations, values, queries))

def rotate(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			matrix[i][j] = matrix[j][i]


matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
  [10,11,12]
]
rotate(matrix)
for i in range(len(matrix)):
	print(matrix[i])
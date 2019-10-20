def searchMatrix(matrix, target):
	if not matrix or not matrix[0]:
		return False
	row, col = 0, len(matrix[0]) - 1
	while col >= 0 and row <= len(matrix) - 1:
		if target == matrix[row][col]:
			return True
		if target < matrix[row][col]:
			col -= 1
		else:
			row += 1
	return False



matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5
print(searchMatrix(matrix,target))
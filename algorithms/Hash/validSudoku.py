def isValidSudoku(board):
	from collections import Counter
	n = len(board)
	# check horizontal lines
	for i in range(n):
		line = board[i]
		temp = Counter(line)
		for key,val in temp.items():
			if key != '.' and val>1:
				return False
	# check vertical lines
	for i in range(n):
		line = [board[j][i] for j in range(n)]
		temp = Counter(line)
		for key,val in temp.items():
			if key != '.' and val>1:
				return False
	# check boxes
	for i in range(0,n,3):
		for j in range(0,n,3):
			box = [board[m][n] for m in range(i,i+3) for n in range(j,j+3)]
			temp = Counter(box)
			for key,val in temp.items():
				if key != '.' and val>1:
					return False 
	return True

board= [[".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]]

print(isValidSudoku(board))
def exist(board,word):
	m = len(board)
	n = len(board[0])
	visited = [[False for _ in range(n)] for _ in range(m)]
	for i in range(m):
		for j in range(n):
			if backtrack(board,word,i,j,visited):
				return True
	return False

def backtrack(board,word,i,j,visited):
	if 0 == len(word):
		return True
	if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!=word[0] \
		or visited[i][j] is True:
		return False
	visited[i][j]=True
	flag = backtrack(board,word[1:],i-1,j,visited) or \
		backtrack(board,word[1:],i+1,j,visited) or \
		backtrack(board,word[1:],i,j-1,visited) or \
		backtrack(board,word[1:],i,j+1,visited)
	visited[i][j]=False
	return flag

board =[['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']]
word = 'ABCB'
print(exist(board,word))

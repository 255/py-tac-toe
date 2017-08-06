board = [[1,2,3],[4,5,6],[7,8,9]]

def printBoard(board):
	horizontalDivider = "---+---+---"
	for row in range(3):
		print("", board[row][0], "|", board[row][1], "|", board[row][2])
		if row != 2:
			print(horizontalDivider)

print("Welcome to Py-Tac-Toe!")
printBoard(board)

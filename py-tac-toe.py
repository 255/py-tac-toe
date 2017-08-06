board = [[1,2,3],[4,5,6],[7,8,9]]

def printBoard(board):
	horizontalDivider = "---+---+---"
	for row in range(3):
		print("", board[row][0], "|", board[row][1], "|", board[row][2])
		if row != 2:
			print(horizontalDivider)

def getTile(board, tile):
	tile = tile - 1
	row = tile // 3
	col = tile % 3
	return board[row][col]

def isValidMove(board, move):
	currentValue = getTile(board, move)
	return currentValue == move

print("Welcome to Py-Tac-Toe!")
printBoard(board)

move = int(input("Your move [1-9]: "))
print(isValidMove(board, move))

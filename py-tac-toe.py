import re

board = [[1,2,3],[4,5,6],[7,8,9]]
validInput = re.compile('^[1-9]$')

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
	if not validInput.match(move):
		return False

	tile = int(move)
	currentValue = getTile(board, tile)
	return currentValue == tile

def applyMove(board, tile, marker):
	tile = tile - 1
	row = tile // 3
	col = tile % 3
	board[row][col] = marker

print("Welcome to Py-Tac-Toe!")
printBoard(board)

userInput = input("You are X. Your move [1-9]? ")
if isValidMove(board, userInput):
	applyMove(board, int(userInput), "X")
	printBoard(board)
else:
	print("Whoops! Your input was invalid, please type a legal move between 1 and 9")

import re
import random

board = [[1,2,3],[4,5,6],[7,8,9]]
validInput = re.compile('^[1-9]$')
statusEnum = {"Deadlock": -1, "No victory": 0, "Victory": 1}
possibleVectors = [
	[1,2,3], [4,5,6], [7,8,9], # all rows
	[1,4,7], [2,5,8], [3,6,9], # all columns
	[1,5,9], [3,5,7] # diagonals
]

def printBoard(board):
	horizontalDivider = "---+---+---"
	for row in range(3):
		print("", board[row][0], "|", board[row][1], "|", board[row][2])
		if row != 2:
			print(horizontalDivider)

def getTile(board, tile):
	row = (tile - 1) // 3
	col = (tile - 1) % 3
	return board[row][col]

def isValidMove(board, move):
	if not validInput.match(move):
		return False

	tile = int(move)
	currentValue = getTile(board, tile)
	return currentValue == tile

def applyMove(board, tile, marker):
	row = (tile - 1) // 3
	col = (tile - 1) % 3
	board[row][col] = marker

def getVectorStatus(tiles):
	values = list(map(lambda tile: getTile(board, tile), tiles))
	if values[0] == values[1] == values[2]:
		return statusEnum["Victory"]
	elif "X" in values and "O" in values:
		return statusEnum["Deadlock"]
	else:
		return statusEnum["No victory"]

def getGameStatus(board):
	gameStatus = statusEnum["Deadlock"]
	for vector in possibleVectors:
		status = getVectorStatus(vector)
		if status == statusEnum["Victory"]:
			gameStatus = status
			break
		elif status == statusEnum["No victory"]:
			gameStatus = status
	return gameStatus

def isGameOver(board, lastPlayer):
	gameStatus = getGameStatus(board)
	if gameStatus == statusEnum["Victory"]:
		printBoard(board)
		print("Victory for player", lastPlayer)
		return True
	elif gameStatus == statusEnum["Deadlock"]:
		printBoard(board)
		print("Cat game - nobody can win")
		return True
	else:
		return False

def getComputerMove(board):
	validMoves = []
	for tile in "123456789":
		if isValidMove(board, tile):
			validMoves.append(tile)
	return int(random.choice(validMoves))

def getPlayerMove(board):
	printBoard(board)
	userInput = input("You are X. Your move [1-9]? ")
	while not isValidMove(board, userInput):
		print("Whoops! Your input was invalid, please type a legal move between 1 and 9")
		userInput = input("You are X. Your move [1-9]? ")
	return int(userInput)

def gameLoop():
	print("Welcome to Py-Tac-Toe!")
	lastPlayer = "O" # X always goes first
	while isGameOver(board, lastPlayer) == False:
		if lastPlayer == "X":
			applyMove(board, getComputerMove(board), "O")
			lastPlayer = "O"
		else:
			applyMove(board, getPlayerMove(board), "X")
			lastPlayer = "X"

gameLoop()
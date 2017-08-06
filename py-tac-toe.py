import re
import random

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

def getVectorStatus(board, tiles):
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
		status = getVectorStatus(board, vector)
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

def getPlayerMove(board, playerMarker):
	printBoard(board)
	requestString = "You are " + playerMarker + ". Your move [1-9]? "
	userInput = input(requestString)
	while not isValidMove(board, userInput):
		print("Whoops! Your input was invalid, please type a legal move between 1 and 9")
		userInput = input(requestString)
	return int(userInput)

def getPlayerMarkerChoice():
	userInput = input("Would you like to go first [1] or second [2]? ")
	while not userInput in ("1", "2"):
		print("Whoops! You must enter '1' or '2'")
		userInput = input("Would you like to go first [1] or second [2]? ")
	if userInput == "1":
		return "X"
	else:
		return "O"

def getOppositeMarker(marker):
	if marker == "X":
		return "O"
	else:
		return "X"

# initialize global variables
validInput = re.compile('^[1-9]$')
statusEnum = {"Deadlock": -1, "No victory": 0, "Victory": 1}
possibleVectors = [
	[1,2,3], [4,5,6], [7,8,9], # all rows
	[1,4,7], [2,5,8], [3,6,9], # all columns
	[1,5,9], [3,5,7] # diagonals
]

def gameLoop():
	board = [[1,2,3],[4,5,6],[7,8,9]]

	# let user decide order of play
	print("Welcome to Py-Tac-Toe!")
	playerMarker = getPlayerMarkerChoice()
	computerMarker = getOppositeMarker(playerMarker)

	# play the game
	lastPlayer = "O" # X always goes first
	while isGameOver(board, lastPlayer) == False:
		if lastPlayer == playerMarker:
			applyMove(board, getComputerMove(board), computerMarker)
			lastPlayer = computerMarker
		else:
			applyMove(board, getPlayerMove(board, playerMarker), playerMarker)
			lastPlayer = playerMarker

gameLoop()

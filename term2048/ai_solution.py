import random
def hole(colrow):
	hole = False
	for i in colrow:
		if i != 0:
			hole = True
		if hole and i == 0:
			return True
	return False
def repeats(colrow):
	b = colrow[0]
	for i in range(1, len(colrow)):
		if b == i:
			return True
		b = i
	return False
def is_empty(colrow):
	for i in colrow:
		if i != 0:
			return False
	return True
def try_left():
	hole_row = -1
	for i in range(len(game.board.cells)): 
		if hole(game.board.cells[i]) or repeats(game.board.cells[i]):
			hole_row = i
	if hole_row != -1:
		return LEFT
	empty_row = -1
	for i in range(len(game.board.cells)): 
		if is_empty(game.board.cells[i]):
			empty_row = i
	if empty_row != -1:
		return DOWN
	raise Exception
def try_down():
	hole_col = -1
	for i in range(len(game.board.cells[0])): 
		if hole(game.board.getCol(i)) or repeats(game.board.getCol(i)):
			hole_col = i
	if hole_col != -1:
		return DOWN
	empty_col = -1
	for i in range(len(game.board.cells[0])): 
		if is_empty(game.board.getCol(i)):
			empty_row = i
	if empty_row != -1:
		return LEFT
	raise Exception
def get_ai_move(game):
	UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4
	downrow = game.board.getLine(3)
	leftcol = game.board.getCol(0)
	if 0 in downrow and 0 in leftcol:
		try:
			return try_left()
		except:
			pass
	if 0 in downrow:
		try:
			return try_down()
		except:
			pass
	if repeats(downrow):
		return LEFT
	if repeats(leftcol):
		return DOWN
	try:
		return try_down()
	except:
		try:
			return try_left()
		except:
			pass
	
	

	""" Useful things:

		game.board - object of class Board

		game.board.cells - 2d array of cells, each cell is an int like 2, 4, 2048 etc

		game.board.getLine(y) - returns line number y
		game.board.getCol(x) - returns col number x
		game.board.getEmptyCells() - returns a list of x,y pairs for all empty cells

	


	Function has to return a swipe direction.

	Example - code returning a random direction:

	return random.choice(UP, DOWN, LEFT, RIGHT)

	"""
	return random.randint(1,4)

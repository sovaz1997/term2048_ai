import random, copy

UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4

def hole(colrow):
	hole = False
	for i in colrow:
		if i == 0 and not(hole):
			hole = True
		if hole and i != 0:
			return True
	return False
def repeats(colrow):
	b = colrow[0]
	for i in range(1, len(colrow)):
		if b == colrow[i] and b != 0:
			return True
		b = colrow[i]
	return False
def is_empty(colrow):
	for i in colrow:
		if i != 0:
			return False
	return True
def try_left(game):
	hole_row = -1
	for i in range(len(game.board.cells)): 
		if hole(game.board.cells[i]) or repeats(game.board.cells[i]):
			hole_row = i
	if hole_row != -1:
		return LEFT
	raise Exception
def try_right(game):
	hole_row = -1
	for i in range(len(game.board.cells)): 
		copyl = game.board.cells[i]
		copyl.reverse()
		if hole(copyl) or repeats(copyl):
			hole_row = i
	if hole_row != -1:
		return RIGHT
	raise Exception
def try_down(game):
	hole_col = -1
	for i in range(len(game.board.cells[0])):
		copyl = game.board.getCol(i)
		copyl.reverse() 
		if hole(copyl) or repeats(copyl):
			hole_col = i
	if hole_col != -1:
		return DOWN
	raise Exception
def get_ai_move(game):
	downrow = game.board.getLine(3)
	leftcol = game.board.getCol(0)
	try:
		return try_down(game)
	except:
		pass
	try:
		return try_left(game)
	except:
		pass
	try:
		return try_right(game)
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

board = [[1, ".", 3], [".", 1, "."], [".", ".", 1]]

def _isValid(row, col):


def solve(board):
	for row in range(3):
		for col in range(3):
			if board[row][col] == ".":
				for i in range(3):
					if _isValid(row, col, i):
						board[row][col] = i
					else:
						#backtrack










solve(board)
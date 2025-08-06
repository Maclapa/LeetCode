#36. Valid Sudoku
# Medium
# Topics
# premium lock icon
# Companies
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

board = [["8","3",".",".","7",".",".",".","."]
,[".",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def check_rows():
    for row in board:
        row_check = []
        for element in row:
                if element in row_check:
                    return False
                elif element != ".":
                    row_check.append(element)
        return True
def check_columns():
    for column in range(len(board)):
        column_check = []
        for row in board:
            element = row[column]
            if element in column_check:
                return False
            elif element != ".":
                column_check.append(element)
        return True
def check_square():
    for i in [0,3,6]:
        for column in range(i,3+i):
            for j in [0,3,6]:
                square_check = []
                for row in board[j:3+j]:
                    element = row[column]
                    if element in square_check:
                        return False
                    elif element != ".":
                        square_check.append(element)
    return True


print(check_rows())
print(check_columns())
print(check_square())



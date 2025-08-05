#According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state:
# live (represented by a 1) or dead (represented by a 0).
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four
# rules (taken from the above Wikipedia article):
#
# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.
#
# Given the current state of the board, update the board to reflect its next state.
#
# Note that you do not need to return anything.

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]


next_stage = [[0 for i in range(len(board[0]))]for i in range(len(board))]

def check(row,column):
    live_neighbours = 0
    for r in range(row-1, row+2):
        for c in range(column-1, column+2):
            if r !=-1 and c!=-1 and r<len(board) and c< len(board[0]):
                if (c != column or r !=row) and board[r][c] == 1:
                    live_neighbours +=1
    return live_neighbours

for row in range(len(board)):
    for column in range(len(board[0])):
        live_neighbours = check(row, column)
        print(f"row: {row}, column: {column}, live neighbours: {live_neighbours}")
        if board[row][column] == 1 and live_neighbours < 2:
            next_stage[row][column] = 0
        elif board[row][column] == 1 and live_neighbours <4:
            next_stage[row][column] = 1
        elif board[row][column] == 1 and live_neighbours >3:
            next_stage[row][column] = 0
        elif board[row][column] == 0 and live_neighbours == 3:
            next_stage[row][column] = 1
print(next_stage)
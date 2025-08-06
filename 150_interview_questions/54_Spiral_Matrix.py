# #Given an m x n matrix, return all elements of the matrix in spiral order.
# # Example 1:
# #
# #
# # Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# # Output: [1,2,3,6,9,8,7,4,5]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
new_matrix = []
rows = len(matrix)
columns = len(matrix[0])
position = (0,0)
direction = "left"
row_number = [i for i in range(rows)]
column_number = [i for i in range(columns)]
while row_number and column_number:
    if position == (0,0):
        direction = "right"
        new_matrix.append(matrix[position[0]][position[1]])
    if direction == "right":
        position = (position[0],position[1] + 1)
    elif direction == "left":
        position = (position[0],position[1] - 1)
    elif direction == "down":
        position = (position[0] + 1, position[1])
    elif direction == "up":
        position = (position[0] - 1, position[1])
    new_matrix.append(matrix[position[0]][position[1]])

    if position[0] == row_number[0] and position[1] == column_number[-1] and direction == "right":
        direction = "down"
        row_number = row_number[1:]
    elif position[0] == row_number[-1] and position[1] == column_number[0] and direction == "left":
        direction = "up"
        row_number = row_number[:-1]
    elif position[0] == row_number[0] and position[1] == column_number[0] and direction == "up":
        direction = "right"
        column_number = column_number[1:]
    elif position[0] == row_number[-1] and position[1] == column_number[-1] and direction == "down":
        direction = "left"
        column_number = column_number[:-1]

print(new_matrix)
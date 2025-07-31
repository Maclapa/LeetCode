# #The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
#
#
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
s = "PAYPALISHIRING"
numRows = 3
matrix = [[0 for i in range(0,len(s))] for i in range(0, numRows)]
current_row, current_column = 0,0
down_direction = False
for i in s:
    matrix[current_row][current_column] = i
    if current_row == 0 or current_row ==2:
        down_direction = not down_direction
    if down_direction:
        current_row = current_row+1
    else:
        current_row = current_row -1
        current_column = current_column +1
print(matrix)
new_string = ""
for i in range(0, numRows):
    new_string += "".join(x for x in matrix[i] if x !=0)

print(new_string)




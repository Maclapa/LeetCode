#Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
# Example 1:
#
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# Example 2:
#
# Input: triangle = [[-10]]
# Output: -10

# Test cases
triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

def min_total(triangle):
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] = min(triangle[i][j] + triangle[i+1][j+1], triangle[i][j] + triangle[i+1][j])
    return triangle[0][0]
print(min_total(triangle))  # Output: 11



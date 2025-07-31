# #Given an m x n matrix, return all elements of the matrix in spiral order.
# # Example 1:
# #
# #
# # Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# # Output: [1,2,3,6,9,8,7,4,5]
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# rows = len(matrix)
# columns = len(matrix[0])
#
# new_matrix = []
# up = False
# left = False
#
# for i in range(0,rows*columns):
#     if left:
#         new_matrix[matrix[]]
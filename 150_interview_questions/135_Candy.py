# #There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# #
# # You are giving candies to these children subjected to the following requirements:
# #
# # Each child must have at least one candy.
# # Children with a higher rating get more candies than their neighbors.
# # Return the minimum number of candies you need to have to distribute the candies to the children.
# #
# #
# #
# # Example 1:
# #
# # Input: ratings = [1,0,2]
# # Output: 5
# # Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# # Example 2:
# #
# # Input: ratings = [1,2,2]
# # Output: 4
# # Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# # The third child gets 1 candy because it satisfies the above two conditions.
#
#
# ratings = [1,0,2]
# candies = [0 for i in ratings]
# for position, value in enumerate(ratings):
#     if position == 0:
#         if ratings[position] > ratings[position+1]:
#             pass
#         else:
#            candies[position] = 1
#     elif position == len(ratings)-1:
#         if ratings[position]> ratings[position-1]:
#             pass
#         else:
#             candies[position] = 1
#     else:
#         if ratings[position] < ratings[position+1] and ratings[position]<ratings[position-1]:
#             candies[position] = 1
#
# print(candies)
# index = candies.index(1)
# print(index)
#
# for i in ratings[index:]:
#
# for i in ratings[index::-1]:
#     print(i)
#You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#
#
# Example 1:
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps


possibles = [1, 2]
n = 5
def take_stair(position):
    if position == n:
        return 1
    if position> n:
        return 0
    result = 0
    for i in possibles:
        result += take_stair(position+i)
    return result



print(take_stair(0))
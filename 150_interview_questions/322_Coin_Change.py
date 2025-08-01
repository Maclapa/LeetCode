#You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
#
#
# Example 1:
#
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1
# Example 3:
#
# Input: coins = [1], amount = 0
# Output: 0


coins = [1,4,5]
res = []
def solution(amount, level):

    if amount<0:
        return 0
    if amount == 0:
        res.append(level)
        return
    for coin in coins:
        new_amount = amount -coin
        solution(new_amount, level+1)
solution(amount=13, level=1)
print(min(res))
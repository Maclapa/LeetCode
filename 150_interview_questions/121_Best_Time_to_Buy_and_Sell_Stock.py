# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

prices = [7,9,5,3,6,4]

l_pointer = 0
r_pointer = 1
income = 0

for l_pointer in range(0,len(prices)-1):
    for r_pointer in  range(l_pointer,len(prices)):
        income = max(prices[r_pointer]-prices[l_pointer], income)

print(income)
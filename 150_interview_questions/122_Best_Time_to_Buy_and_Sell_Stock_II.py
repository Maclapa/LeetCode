# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
#
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
#
# Find and return the maximum profit you can achieve.


# prices = [7,1,5,3,6,4]
prices = [1,2,3,4,6]
max = 0
start = prices[0]
len1 = len(prices)
for i in range(0, len1):
    if start < prices[i]:
        max += prices[i] - start
    start = prices[i]
print(max)
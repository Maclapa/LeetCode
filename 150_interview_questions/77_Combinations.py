#Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
#
# You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

n = 4
k = 3
n_list = [i for i in range(1,n+1)]

res = []

def backtrack(comb, start):
    if len(comb) == k:
        res.append(comb.copy())
        return
    for i in range(start, n+1):
        comb.append(i)
        backtrack(comb, i+1)
        comb.pop()

backtrack(comb=[],start=1)
print(res)

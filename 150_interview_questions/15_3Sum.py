#Given an integer array nums, return all the triplets
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
from copy import copy

# Notice that the solution set must not contain duplicate triplets.
#
#
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

nums = [-1,0,1,2,-1,-4]
results = []
for position_i, value_i in enumerate(nums[:len(nums)-2]):
    for position_j, value_j in enumerate(nums[position_i+1:len(nums)-1]):
        for position_k, value_k in enumerate(nums[position_i+position_j+2:]):
            if value_i + value_j + value_k == 0:
                results.append([value_i, value_j, value_k])
print(results)

sorted_list = [sorted(i) for i in results]
new_list = copy(sorted_list)
distinc_list = []
for i in sorted_list:
    new_list.pop(0)
    if i not in new_list:
        distinc_list.append(i)
print(distinc_list)

#Given an integer array nums, find the subarray with the largest sum, and return its sum.
#
# Example 1:
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:
#
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

nums = [1]
result = []

for position_i, value_i in enumerate(nums):
    sub_array_max = value_i
    for position_j, value_j in enumerate(nums[position_i:]):
        sub_array_max = max(sub_array_max, sum(nums[position_i:position_i+position_j+1]))
    result.append(sub_array_max)

print(max(result))
#Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.
# Example 1:
#
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
#
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
result = []
nums = [-2,0,-1]

def count_product(array):
    result = None
    for i, value in enumerate(array):
        if i == 0:
            result = value
        else:
            result = result*value
    return result

for position_i, value_i in enumerate(nums):
    sub_array_max = value_i
    for position_j, value_j in enumerate(nums[position_i:]):
        sub_array_max = max(sub_array_max, count_product(nums[position_i:position_i+position_j+1]))
    result.append(sub_array_max)

print(max(result))
#209. Minimum Size Subarray Sum

#Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:
#
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

nums = [2,3,1,2,4,3]
target = 7

l_pointer = 0
r_pointer = 0
min_array = nums
sum = nums[0]
while r_pointer!=len(nums)-1 or l_pointer!=len(nums)-1:
    if sum == target:
        if len(min_array) > len(nums[l_pointer:r_pointer+1]):
            min_array = nums[l_pointer:r_pointer+1]
    if sum >= target:
        sum -= nums[l_pointer]
        l_pointer +=1
        continue
    if sum <target:
        sum = sum + nums[r_pointer+1]
        r_pointer +=1
        continue

print(min_array)
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

nums = [1,2,3,5,5,5,5,5,5,7,7]

for i in nums:
   if len(nums) - nums.count(i) < len(nums)/2:
       print(i)
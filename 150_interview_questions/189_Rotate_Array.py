# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

nums = [x for x in range(0,10)]
k=3
print(nums[len(nums)-k:len(nums)])
print(nums[:len(nums)-k])
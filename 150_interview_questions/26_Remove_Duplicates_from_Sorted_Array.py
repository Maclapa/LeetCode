# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
#
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

nums = [1,1,2,2,2,2,2,2,3,4,4,4,4,4,4,4,5,6]

l_pointer = 0
r_pointer = 1

for i in range(0, len(nums)-1):
    if nums[l_pointer] == nums[r_pointer]:
        value = nums[r_pointer]
        nums.pop(r_pointer)
        nums.append(value)
    else:
        l_pointer=l_pointer+1
        r_pointer=r_pointer+1

print(nums)
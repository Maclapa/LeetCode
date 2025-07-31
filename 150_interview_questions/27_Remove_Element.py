# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
#
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
#
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.


nums = [1,2,2,3,4,5,6]
val = 2
pointer = 0
for numbers in nums:
    if nums[pointer] == val:
        nums.pop(pointer)
        nums.append(val)
    else:
        pointer = pointer+1

print(pointer)
print(nums[0:pointer])


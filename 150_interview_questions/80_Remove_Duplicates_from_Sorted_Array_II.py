# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.



nums = [1,1,1,2,2,2,2,2,2,3,4,4,4,4,4,4,4,5,6]

l_pointer = 0
r_pointer = 1
repetition_number = 2
found_number = 0
for i in range(0, len(nums)-repetition_number):
    if nums[l_pointer] == nums[r_pointer]:
        found_number = found_number+1
        if repetition_number == found_number:
            value = nums[r_pointer]
            nums.pop(r_pointer)
            nums.append(value)
            found_number = 1
        else:
            r_pointer = r_pointer+1
    else:
        found_number = 0
        l_pointer=r_pointer
        r_pointer=r_pointer+1

print(nums)
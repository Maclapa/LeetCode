#You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array
# represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

#

nums = [2,2,1,0,4]

position = 0
end_position = len(nums)-1

for i in range(len(nums)-2,-1,-1):
    if nums[i] == 0:
        continue
    if nums[i] >= end_position-i:
        end_position = i
    if end_position ==0:
        print("There is a solution")



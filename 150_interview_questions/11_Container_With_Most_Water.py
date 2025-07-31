#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:
#
# Input: height = [1,1]
# Output: 1

height = [1,1]

l_pointer = 0
r_pointer = len(height)-1
max_volume = 0
for i in height:
    current_volume = min(height[l_pointer], height[r_pointer])*(r_pointer - l_pointer)
    max_volume = max(max_volume, current_volume)
    if height[l_pointer]> height[r_pointer]:
        r_pointer = r_pointer-1
    else:
        l_pointer = l_pointer+1
print(max_volume)

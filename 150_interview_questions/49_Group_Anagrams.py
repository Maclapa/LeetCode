# #Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# #
# # Example 1:
# #
# # Input: strs = ["eat","tea","tan","ate","nat","bat"]
# #
# # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# #
# # Explanation:
# #
# # There is no string in strs that can be rearranged to form "bat".
# # The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# # The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
#
strs = ["eat","tea","tan","ate","nat","bat"]
output = []
for position_i, value_i in enumerate(strs):
    result_array = []
    for position_j, value_j in enumerate(strs[position_i+1:]):
        if sorted(value_i) == sorted(value_j):
            result_array.append(value_j)
            strs.pop(position_j)
    result_array.append(value_i)
    output.append(result_array)

print(output)
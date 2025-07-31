#Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
prefixes = []
strs = ["flower","flow","floight"]
for word in strs[1:]:
    prefix = ""
    for letter_number, letter in enumerate(strs[0]):
        if prefix + letter != word[:letter_number+1]:
            break
        prefix = prefix + letter
    prefixes.append(prefix)

final_prefix = sorted(prefixes)[0]
print(final_prefix)


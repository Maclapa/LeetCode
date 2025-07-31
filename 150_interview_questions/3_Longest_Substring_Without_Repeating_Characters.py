#Given a string s, find the length of the longest substring without duplicate characters.


#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
s = "abcabcddebb"
longest_substring = ""
r_pointer = 0
l_pointer = 0
new_longest = ""

while r_pointer != len(s)-1 or l_pointer != len(s)-1:
    if s[r_pointer] not in longest_substring:
        longest_substring = longest_substring + s[r_pointer]
        if len(longest_substring) > len(new_longest):
            new_longest = longest_substring
        r_pointer +=1
    else:
        longest_substring = longest_substring[1:]
        print(longest_substring)
        l_pointer += 1

print(new_longest)
#Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
#
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
#
#
# Example 1:
#
# Input: pattern = "abba", s = "dog cat cat dog"
#
# Output: true
#
# Explanation:
#
# The bijection can be established as:
#
# 'a' maps to "dog".
# 'b' maps to "cat".

pattern = "abba"
s = "dog cat cat dog"
s = s.split()
print(s)
new_map = {}

for position, value in enumerate(pattern):
    if value in new_map.keys():
        if new_map[value] != s[position]:
            print(False)
            break
    else:
        new_map[value] = s[position]
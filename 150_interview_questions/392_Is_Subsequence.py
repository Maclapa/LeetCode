#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
# characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of
# "`abcde`" while "aec" is not).

s = "ace"
t = "abcde"

dictionary = {}

for i in s:
    if i not in t:
        break
    else:
        dictionary[i] = t.find(i)
dictionary_values = [value for value in dictionary.values()]
assert len(dictionary.keys()) == len(s)
assert dictionary_values == sorted(dictionary_values)




#Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.
#
#
#
# Example 1:
#
# Input: ransomNote = "a", magazine = "b"
# Output: false


ransomNote = "aac"
magazine = "aabc"
match = False
for i in ransomNote:
    if i in magazine:
        magazine = magazine.replace(i, "",1)
        match = True
    else:
        match = False

print(match)
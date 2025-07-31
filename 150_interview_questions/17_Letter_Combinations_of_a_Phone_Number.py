#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

numbers = {"2": "abc", "3": "def"}
digits = "23"
res = []

def backtrack(i, text):
    if len(text) == len(digits):
        res.append(text)
        return

    for c in numbers[digits[i]]:
        backtrack(i+1, text+c)

backtrack(0, "")
print(res)
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#
# Input: s = "([{}])"
#
# Output: true

s ="()"
stack = []

for i in s:
    if i == "(":
        stack.append(i)
    if i == "{":
        stack.append(i)
    if i == "[":
        stack.append(i)
    if i == ")":
        if stack[-1] == "(":
            stack.pop()
        else:
            print("ZLE")
    if i == "}":
        if stack[-1] == "{":
            stack.pop()
        else:
            print("ZLE")
    if i == "]":
        if stack[-1] == "[":
            stack.pop()
        else:
            print("ZLE")

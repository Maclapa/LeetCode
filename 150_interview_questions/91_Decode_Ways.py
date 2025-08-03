# #You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:
#
# "1" -> 'A'
#
# "2" -> 'B'
#
# ...
#
# "25" -> 'Y'
#
# "26" -> 'Z'
#
# However, while decoding the message, you realize that there are many different ways you can decode the message
# because some codes are contained in other codes ("2" and "5" vs "25").
#
# For example, "11106" can be decoded into:
#
# "AAJF" with the grouping (1, 1, 10, 6)
# "KJF" with the grouping (11, 10, 6)
# The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
# Note: there may be strings that are impossible to decode.
#
# Given a string s containing only digits, return the number of ways to decode it.
# If the entire string cannot be decoded in any valid way, return 0.
#
# Example 1:
#
# Input: s = "12"
#
# Output: 2
#
# Explanation:
#
# "12" could be decoded as "AB" (1 2) or "L" (12).
#
# Example 2:
#
# Input: s = "226"
#
# Output: 3
#
# Explanation:
#
# "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

s = "06"
dp =[0]*len(s)
for pos,value in enumerate(s):
    if pos ==0 and value=="0":
        print("zero")
    if pos>0 and int(s[pos-1:pos+1]) <27:
        if int(s[pos-1]) != 0:
            dp[pos] = dp[pos-1]+1
    elif value == 0 and pos-1>=0:
        dp[pos] = dp[pos-1]
    else:
        dp[pos] = max(1, max(dp)+1)
print(max(dp))
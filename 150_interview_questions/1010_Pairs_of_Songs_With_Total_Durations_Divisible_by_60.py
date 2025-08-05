#You are given a list of songs where the ith song has a duration of time[i] seconds.

# Return the number of pairs of songs for which their total duration in seconds is divisible by 60.
# Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
# Example 1:
#
# Input: time = [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60

time = [60,60,60]
res = []
for position_i, value_i in enumerate(time[:-1]):
    for position_j, value_j in enumerate(time[position_i+1:]):
        if (value_i + value_j) % 60 == 0:
            res.append([position_i, position_j+position_i])

print(len(res))
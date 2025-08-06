# Design a hit counter which counts the number of hits received in the past 5 minutes.
#
# Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made
# to the system in chronological order (ie, the timestamp is monotonically increasing).
# You may assume that the earliest timestamp starts at 1.
#
# It is possible that several hits arrive roughly at the same time.


class HitCounter:
    def __init__(self):
        self.dict_hit = {}

    def hit(self, timestamp):
        self.dict_hit[timestamp] = 1

    def get(self, timestamp):
        count = 0
        for key in self.dict_hit.keys():
            if timestamp - key < 300:
                count+=1
        return count

counter = HitCounter()
counter.hit(1)
print(counter.get(302))
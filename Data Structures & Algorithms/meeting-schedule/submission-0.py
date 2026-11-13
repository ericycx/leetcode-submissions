"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        all_intervals = []
        for interval in intervals:
            all_intervals.append([interval.start,interval.end])
        all_intervals.sort(key=lambda x: x[1])
        print(all_intervals)
        for i in range(1, len(all_intervals)):
            if all_intervals[i][0] < all_intervals[i-1][1]:
                return False
        return True

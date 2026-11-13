"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        ends = []
        for iv in intervals:
            if ends and ends[0] <= iv.start:
                heapq.heapreplace(ends, iv.end)
            else:
                heapq.heappush(ends, iv.end)      # open a new room
        return len(ends)

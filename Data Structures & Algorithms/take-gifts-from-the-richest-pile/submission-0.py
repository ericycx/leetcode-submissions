import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)
        for i in range(k):
            thing = heapq.heappop_max(gifts)
            heapq.heappush_max(gifts,math.floor(thing ** 0.5))
        return sum(gifts)
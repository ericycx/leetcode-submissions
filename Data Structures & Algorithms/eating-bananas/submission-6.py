class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = 1
        m = max(piles) # O(n)
        while n <= m:
            mid = (n + m) // 2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/mid)
            if total_hours <= h:
                m = mid - 1
            elif total_hours > h:
                n = mid + 1
        return n
        
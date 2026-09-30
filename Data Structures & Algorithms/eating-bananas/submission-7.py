class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = 1
        m = max(piles) # O(n)
        while n <= m:
            mid = (n + m) // 2
            total_hours = 0
            for pile in piles:
                total_hours += (pile + mid - 1) // mid
            if total_hours <= h:
                m = mid - 1
            else:
                n = mid + 1
        return n
        
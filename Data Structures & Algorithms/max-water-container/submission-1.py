class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n - 1
        max_height = 0
        while i < j:
            distance = j - i
            max_area = distance * min(heights[i],heights[j])
            max_height = max(max_area,max_height)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return max_height

class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        if not height:
            return trapped
        i = 0
        j = len(height) - 1
        max_left = height[i]
        max_right = height[j]
        while i < j:
            if height[i] > height[j]:
                trapped += min(max_left, max_right) - height[j]
                j -= 1
                max_right = max(max_right, height[j])
            else:
                trapped += min(max_left, max_right) - height[i] 
                i += 1
                max_left = max(max_left, height[i])
        return trapped
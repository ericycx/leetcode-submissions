class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        local = 0
        for ch in s:
            if ch == '(':
                local += 1
            elif ch == ')':
                local -= 1
            depth = max(depth, local)
        return depth
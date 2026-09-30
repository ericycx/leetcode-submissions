class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        close_to_open = {')': '(', '}': '{', ']': '['}
        
        for c in s:
            if c not in close_to_open:
                stack.append(c)
            else:
                if not stack or stack.pop() != close_to_open[c]:
                    return False
        
        return not stack
class Solution:
    def scoreOfString(self, s: str) -> int:
        prev = None
        res = 0
        for ch in s:
            if prev:
                print(ord(ch), ord(prev))
                res += abs(ord(prev) - ord(ch))
            prev = ch
        return res

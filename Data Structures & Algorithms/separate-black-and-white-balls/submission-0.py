class Solution:
    def minimumSteps(self, s: str) -> int:
        cur = 0
        res = 0
        for i in range(len(s)):
            if s[i] == '0':
                res += (i - cur)
                cur += 1
        return res


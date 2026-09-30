class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        seen = {}
        i = 0
        j = 0
        if not s:
            return 0
        while j < len(s):
            if s[j] not in seen:
                seen[s[j]] = j
                max_length = max(max_length, j - i + 1)
            elif s[j] in seen and seen[s[j]] >= i:
                i = seen[s[j]] + 1
                seen[s[j]] = j
                max_length = max(max_length, j - i + 1)
            else:
                seen[s[j]] = j
                max_length = max(max_length, j - i + 1)
            j += 1
        return max_length

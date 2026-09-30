class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0
        i = 0
        max_freq = 0
        for j in range(len(s)):
            count[s[j]] = count.get(s[j], 0) + 1
            max_freq = max(max_freq, count[s[j]])

            while (j - i + 1) - max_freq > k:
                count[s[i]] -= 1
                i += 1
            
            longest = max(longest, j - i + 1)

        return longest
        
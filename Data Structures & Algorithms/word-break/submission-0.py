class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        H = [True] +[False] * (n + 1)
        for i in range(1,n + 1):
            for word in wordDict:
                m = len(word)
                if m <= i and m <= n and not H[i]:
                    H[i] = (H[i - m] and s[i-m:i] == word)
        return H[n]
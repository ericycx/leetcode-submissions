class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        i = 31
        while i >= 0:
            if (n - (2 ** i)) >= 0:
                n = n - (2 ** i)
                count += 1
            i -= 1
        return count
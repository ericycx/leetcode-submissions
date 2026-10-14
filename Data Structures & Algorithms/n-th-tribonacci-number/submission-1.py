class Solution:
    def tribonacci(self, n: int) -> int:
        H = [0] * (n + 4)
        H[0] = 0
        H[1] = 1
        H[2] = 1
        if n < 3:
            return H[n]
        else:
            for i in range(3, n + 1):
                H[i] = H[i - 1] + H[i-2] + H[i-3]
        return H[n]
            
class Solution:
    def numSquares(self, n: int) -> int:
        sqrd = []
        for i in range(1, 101):
            sqrd.append(i ** 2)
        H = [0] * (n + 1)
        H[0] = 0
        for i in range(1, n + 1):
            cur = 9999999
            for sqr in sqrd:
                if sqr <= i:
                    cur = min(cur, 1 + H[i - sqr])
                else:
                    break
            H[i] = cur
        return H[n]

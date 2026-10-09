class Solution:
    def climbStairs(self, n: int) -> int:
        H = [0] * (n + 2)
        H[1], H[2] = 1,2
        for i in range(3, n + 1):
            H[i] = H[i-1] + H[i - 2]
        return H[n]
                

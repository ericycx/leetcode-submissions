class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        H = [[1] * n for _ in range(m)] 
        for i in range(n):
            H[0][i] = 1
        for j in range(m):
            H[j][0] = 1
        for i in range(1,n):
            for j in range(1,m):
                H[j][i] = H[j][i-1] + H[j-1][i]
        print(H)
        return H[m-1][n-1]

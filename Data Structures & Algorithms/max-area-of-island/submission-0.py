class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        m = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count = 1
                    queue = deque([(i,j)])
                    grid[i][j] = 0
                    while queue:
                        x,y = queue.popleft()
                        for dx,dy in directions:
                            nx,ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                                grid[nx][ny] = 0
                                count += 1
                                queue.append((nx, ny))
                    res = max(res,count)
        return res
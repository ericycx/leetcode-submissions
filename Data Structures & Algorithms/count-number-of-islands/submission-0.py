class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        n = len(grid)
        m = len(grid[0])
        count = 0
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def bfs(x,y):
            queue = deque([(x,y)])
            seen.add((x,y))
            while queue:
                curx, cury = queue.popleft()
                for dx,dy in directions:
                    nx,ny = curx + dx, cury + dy
                    if (nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] == "0"):
                        pass
                    elif (nx,ny) not in seen:
                        seen.add((nx,ny))
                        queue.append((nx,ny))
            return
        for i in range(n):
            for j in range(m):
                if (i,j) not in seen and grid[i][j] == "1":
                    count += 1
                    bfs(i,j)
        return count
                    


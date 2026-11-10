class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        def bfs(row, col):
            dque = deque([(row,col)])
            visited.add((row,col))
            perimeter = 0
            while dque:
                x,y = dque.popleft()
                for dx, dy in directions:
                    nx,ny = x + dx, y + dy
                    if (nx < 0 or ny < 0 or nx >= rows or ny >= columns or grid[nx][ny] == 0):
                        perimeter += 1
                    elif (nx,ny) not in visited:
                        visited.add((nx,ny))
                        dque.append((nx,ny))
            return perimeter
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    return bfs(i,j)
        return 0

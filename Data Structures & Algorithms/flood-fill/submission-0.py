class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        cur_colour = image[sr][sc]

        def bfs(r,c):
            queue = deque([(r, c)])
            visited.add((r,c))

            while queue:
                curx,cury = queue.popleft()
                image[curx][cury] = color

                for dx,dy in directions:
                    nx, ny = curx + dx, cury + dy
                    if (nx < 0 or nx >= m or ny < 0 or ny >= n or image[nx][ny] != cur_colour) or image[nx][ny] == color:
                        pass
                    elif image[nx][ny] not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            return
        bfs(sr,sc)
        return image

                    
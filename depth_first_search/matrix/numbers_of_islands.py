"""
No. of islands count is process of counting connected 1s in a grid as one island
and find all islands in the grid

We can DFS 
"""
from collections import deque
class Solution:
    def numerOfIslands(self, grid):
        def dfs(i, j):
            nonlocal rows, cols
            queue = deque([(i, j)])
            while(queue):
                r, c = queue.popleft()
                visited.add((r, c))
                for nr, nc in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 \
                        and (nr, nc) not in visited:
                        queue.append((nr, nc))

        visited = set()
        rows, cols = len(grid), len(grid[0])
        islands_count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    islands_count += 1
                    dfs(i, j)
        
        return islands_count

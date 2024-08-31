"""
idea is find all the surrounded regions.
a surrounded region is a region if all 'O' of that region are surronded by 'X'
if 'O' is in boder then it cannot be surrounded and it is considered 'S' safe.

Solution approach:
find all the bordering 0. marked them safe and find all the connected 0 and marked them safed as well
then rest of grid, find all 0 and change them x and 
S one converted back to 0
"""
class Solution:
    def surrounded_region(self, grid):
        rows, cols = len(grid), len(grid[0])
        def dfs(i, j):
            nonlocal rows, cols
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 'O':
                grid[i][j] = 'S'
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)
        
        for i in range(rows):
            if grid[i][0] == 'O':
                dfs(i, 0)
            if grid[i][cols - 1] == 'O':
                dfs(i, cols - 1)
        
        for j in range(cols):
            if grid[0][j] == 'O':
                dfs(0, j)
            if grid[rows - 1][j] == 'O':
                dfs(rows - 1, j)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'O':
                    grid[i][j] = 'X'
                if grid[i][j] == 'S':
                    grid[i][j] = 'O'
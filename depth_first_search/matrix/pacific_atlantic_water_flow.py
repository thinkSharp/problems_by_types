"""
find cells in the grid where rain water can flow both pacific and atlantic oceans.
a cell can flow to ocean if it is connected to the ocean or a cell with equal to or low no.

Solution approach:
identify ocean connected cells, we know they can flow through either one of both of them
start from those cells and recusively find other cells
"""
from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])
        pacific_access = set()
        atlantic_access = set()

        def dfs (r, c, access):
            access.add((r, c))
            for nr, nc in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in access \
                    and heights[nr][nc] <= heights[r][c]:
                    dfs(nr, nc, access)
                    
        for r in range(rows):
            dfs(r, 0, pacific_access)
            dfs(r, cols - 1, atlantic_access)
        
        for c in range(cols):
            dfs(0, c, pacific_access)
            dfs(rows - 1, c, atlantic_access)

        return list(pacific_access & atlantic_access)
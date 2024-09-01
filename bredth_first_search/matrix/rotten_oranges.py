"""
Identify how many minutes it will take to rotten all oranges in the box
if a fresh orange is next to rott organge, it will rott. 
if a fresh orange is surrounded by empty space it will survive.

Goal is to get all the position of rotten oranges and count fresh orange.
using BFS, go through 4 direction to rott all fresh oranges
if end que and still fresh orange left return -1
"""
from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        fresh_count = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    rotten.append([i, j])

        queue = deque([])
        visited, minutes = set(), 0
        if len(rotten) > 0:
            queue.append(rotten)

        while queue:
            rotten_o = queue.popleft()
            rot_count = 0
            fresh_neighbor = []

            for ri, rj in rotten_o:
                if (ri, rj) in visited:
                    continue

                if grid[ri][rj] == 1:
                    rot_count += 1
                    grid[ri][rj] = 2

                visited.add((ri, rj))

                for fi, fj in [[ri + 1, rj], [ri - 1, rj], [ri, rj + 1], [ri, rj - 1]]:
                    if 0 <= fi < rows and 0 <= fj < cols and (fi, fj) not in visited:
                        if grid[fi][fj] == 1:
                            fresh_neighbor.append([fi, fj])

            if len(fresh_neighbor) > 0:
                queue.append(fresh_neighbor)

            if rot_count > 0:
                minutes += 1
                fresh_count -= rot_count
        return minutes if fresh_count == 0 else -1

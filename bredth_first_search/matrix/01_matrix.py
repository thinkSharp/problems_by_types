"""
calculate distance of all nearest zeros from ones cell.
if no zeros in the grid, return -1
Solution approach:
check if how many zeros and capture the location of 1s
if zeros count is 0 then create matrix with -1 and return
else, create BFS queue to start calculating all 0s and calculate distance of 1s
"""
from collections import deque
from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat
        rows, cols = len(mat), len(mat[0])
        curr_list = []
        queue, visited = deque([]), set() 
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    curr_list.append([i, j])
                else:
                    mat[i][j] = -1
        if len(curr_list) > 0:
            queue.append(curr_list)
        
        while queue:
            proc_list = queue.popleft()
            curr_list = []
            for ci, cj in proc_list:
                visited.add((ci, cj))
                val = mat[ci][cj]
                for ni, nj in [[ci - 1, cj], [ci + 1, cj], [ci, cj - 1], [ci, cj + 1]]:
                    if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited and mat[ni][nj] == -1:
                        mat[ni][nj] = val + 1
                        curr_list.append([ni, nj])
                        visited.add((ni, nj))
            if len(curr_list) > 0:
                queue.append(curr_list)
        return mat




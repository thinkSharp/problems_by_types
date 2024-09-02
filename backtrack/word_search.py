"""
idea is to loop through the grid and check the current cell maches the char we are looking for
if it does then look for 4 direction for next word.
if not backtrack and prune the current path.
contine until we found the word or end of the loop

bleed
B L C H
D E L T
D A K A

"""
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        
        rows, cols, word_len = len(board), len(board[0]), len(word)
        visited = set()

        def backtrack(i, j, word_index):
            if word_index >= word_len:
                return True
            
            if board[i][j] != word[word_index]:
                return False
            
            visited.add((i, j))
            for ni, nj in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited:
                    completed = backtrack(ni, nj, word_index + 1)
                    if completed:
                        return True
            visited.pop()
            return False
        
        for i in range(rows):
            for j in range(cols):
                completed = backtrack(i, j, 0)
                if completed:
                    return True
                
        return False
    

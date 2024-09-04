"""
using dynamic programming
initialize dep to n +1 and c + 1
loop through the grid and update dp position
return last dp position
formula top, left, -1, -1 get min + current if current == '1'

"""
from typing import List
class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_square = 0
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        if rows == 1 and cols == 1:
            return 1 if matrix[0][0] == '1' else 0
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                min_ = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
                val = int(matrix[i - 1][j - 1])
                dp[i][j] = min_ + val if val > 0 else 0
                max_square = max(max_square, dp[i][j])
        return max_square ** 2
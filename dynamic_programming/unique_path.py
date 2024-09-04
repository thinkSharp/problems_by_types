"""
Unique path calculation using dynamic programming using bottom up approach
- initialize dp same size as table with 1s
- start calculating using following formula row - 1 + col - 1

"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
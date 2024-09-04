"""

"""
from typing import List
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)

        combined = list(zip(startTime, endTime, profit))
        sorted_combined = sorted(combined, key=lambda x: x[1])
        startTime, endTime, profit = map(list, zip(*sorted_combined))
        dp = profit[:]
        print(startTime)
        print(endTime)
        print(profit)
        for i in range(1, n):
            for j in range(i):
                if endTime[j] <= startTime[i]:
                    dp[i] = max(dp[i], profit[i] + dp[j])

        return max(dp)
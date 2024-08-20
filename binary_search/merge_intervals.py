"""
merge intervals group together all the overlapping intervals
in order to merge properly sort all intervals by end time
check last with first of next, if last >= first merge
Time comlexity o(nlogn)
Space complexity o(n) for sorting

Example: [(1,3),(2,6),(8,10), (15,18)]
result = [[1,6],[8,10], [15,18]]

[[1,4],[4,5]]
result = [[1,5]]
"""
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result =[intervals[0]]
        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                if intervals[i][1] > result[-1][1]:
                    result[-1][1] = intervals[i][1]
            else:
                result.append(intervals[i])

        return result
    
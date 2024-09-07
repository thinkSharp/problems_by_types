"""
how does sert inerval would work?
first sort the original list
then insert the new interval. 
then adjust intervals by removing the overlapping ones
Time complexity is O(n)
Space complexity is O(1)
"""
class Solution:
    def insertintervals(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        n = len(intervals)
        merged = []
        i = 0

        # get all intervals with end time less then start time of newIntervals
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # check for overlap with new intervals
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        merged.append(newInterval)
        for j in range(i, n):
            merged.append(intervals[j])

        return merged
     
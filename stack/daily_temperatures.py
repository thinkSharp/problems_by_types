"""
in order to find no. of days to wait for a warmer temperatures,
use monoeastic stack to keep track of temperature until a warmer days
ex: [73, 74, 75, 71, 69, 72, 76, 73]
res [1, 1, 4, 2, 1, 1, 0, 0]
stack[0]
stack[1]
stack[2]
stack[2,3]
stack[2,3,4]
stack[6]
stack[6,7]

Time complexity : O(n)
space complexity: O(n)
"""
from typing import List
class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and temps[i] > temps[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result


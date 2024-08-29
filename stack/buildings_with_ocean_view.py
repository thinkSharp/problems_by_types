"""
finding building with ocean view:
building has ocean view if all the right hand side building are small then current
solution approach:
loop from back and check to see if a building is ocean view
if empty stack or stack[-1] < heights[i]:
 pop()
 append i in result
 add to stack

 return result[::-1]
"""
from typing import List
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result, stack = [], []
        for i in range(len(heights) - 1, -1, -1):
            if not stack or heights[stack[-1]] < heights[i]:
                result.append(i)
                stack.append(i)
        return result[::-1]
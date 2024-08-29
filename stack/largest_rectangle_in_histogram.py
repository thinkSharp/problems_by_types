"""
in order to find the largest rectangle area of the histogram,
stack will be utilized. 
add index of the hight until a smaller one is encountered
then calculate the area.
At the end clean the stack to ensure that all scenarios are covered

[2, 1, 5, 6, 2, 3]

stack: [0] a: 0
stack: [1] a: 2
stack: [1,2] a: 2
stack: [1,2,3] a: 2
stack: [1,2] a: 6
stack: [1] a: 10
stack: [1,2] a: 10
stack: [1,2,3] a: 10

stack: [1,2] a: 10
stack: [1] a: 10
stack: [] a: 10
"""
from typing import List
class Solution:
    def largest_rectangle_area(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        i = 0
        while i < len(heights):
            if not stack or stack[-1] < heights[i]:
                stack.append(i)
                i += 1
            else:
                idx = stack.pop()
                right = i - 1
                left = stack[-1] if stack else -1
                area = heights[idx] * (right - left)
                max_area = max(max_area, area)
        while stack:
            idx = stack.pop()
            width = i - stack[-1] - 1 if stack else  i
            area = width * heights[idx]
            max_area = max(max_area, area)

        return max_area
    

    

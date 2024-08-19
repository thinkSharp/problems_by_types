"""
move zero while maintaining the relative position of non_zero elements
z = 0
[1, 3, 12, 0, 0]
       z
                 i

                 
[1,3,2,3,1,0,0, 0, 0]
         z
                   i
"""
from typing import List
class Solution:
    def moveZeros(self, nums: List[int]) -> None:
        z = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[z] = nums[z], nums[i]
                z += 1
        return nums
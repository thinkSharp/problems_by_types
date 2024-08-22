"""
moving zeros
moving zeros using two pointers technique
i, j both pointing to index 0 initially
if nums[j]  != 0:
    swap
    move i

[1, 3, 12, 0, 0]
       i
              j
"""
from typing import List
class Solution:
    def moveZeros(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        
"""
Array is sorted:
remove duplicate inplace
return k which is unique elements
[0,1,2,3,4,2,2,3,3,4]
           i
                     j
   
"""
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1
        
        return i
    

if __name__ == '__main__':
    sol = Solution()

    assert(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) == 5


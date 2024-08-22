"""
next permutation
steps to identify the next permutation
- find the first decreasing element from the back
- swap that smallest element larger then pivot
- then reverse the sequence after the swap index

[1, 4, 3, 2]
 i

 smallest index: 3 ==> value 2

 [2, 4, 3, 1]

 reverse [4,3,1]

 answer is [2,1,3,4]

 [2,1]

  [1,2,3,4,6,5]
   [4,3,2,1]
"""
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int] ) -> None:
        if len(nums) == 1:
            return None
        
        for j in range(len(nums) - 2, -1, -1):
            if nums[j] < nums[j + 1]:
                small = len(nums) -1
                while small > j:
                    if nums[small] > nums[j]:
                        break
                    else:
                        small -= 1
                nums[j], nums[small] = nums[small], nums[j]
                nums[j+1:] = nums[j+1:][::-1]
                return None


        nums[::] = nums[::-1]
        return None

if __name__ == '__main__':
    sol = Solution()

    val = [2,3,1]
    sol.nextPermutation(val)
    print(val)
    val = [1,2,3,4]
    sol.nextPermutation(val)
    print(val)
    val = [1,2]
    sol.nextPermutation(val)
    print(val) 
    val = [4,3,2,1]
    sol.nextPermutation(val)
    print(val)
    val = [1,5,5,3,2]
    sol.nextPermutation(val)
    print(val)


"""
[-1, 0, 1,2,-1,-4]
[-4, -1, -1, 0, 1, 2]
             i
                j        
                   k
[-1, -1, 2] , [-1, 0, 1]        
"""
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total > 0:
                    k -= 1
                    continue
                elif total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                else:
                    j += 1

                while j < k and nums[j] == nums[j - 1]:
                    j += 1

        return result
    

if __name__ == '__main__':
    sol = Solution()

    assert(sol.threeSum([-1,0,1,2,-1,-4])) == [[-1, -1, 2], [-1, 0, 1]]
    assert(sol.threeSum([0, 1, 1])) == []
    assert(sol.threeSum([0,0,0])) == [[0, 0, 0]]

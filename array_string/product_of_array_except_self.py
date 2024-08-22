"""
product of array multiply self
[3,4,2,3]
[1,3,12,24]
[24,6,3,1]
[24,18,36,24]

left[i] = left[i - 1] * s[i - 1]
right[i] = right[i + 1] * s[i + 1]
ans[i] = left[i] * right[i]

time complexity O(n)
space O(n)
1 2 3 4
1 1 2 6 
6, 8,12,24 

r: 24

-1 1 0 -3 3
1 -1 -1 0 0
0, 0, 9, 0, 0 
r: 0
"""
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        if nums_len == 0:
            return []
        answer = [0] * nums_len
        answer[0] = 1
        for i in range(1, nums_len):
            answer[i] = answer[i - 1] * nums[i - 1]
        
        R = 1
        for j in range(nums_len - 1, -1, -1):
            answer[j] = answer[j] * R
            R *= nums[j]
            
        return answer        

if __name__ == '__main__':
    sol = Solution()

    assert(sol.productExceptSelf([1,2,3,4])) == [24,12,8,6]
    assert(sol.productExceptSelf([-1,1,0,-3,3])) == [0,0,9,0,0]
    print('Hello Wold')
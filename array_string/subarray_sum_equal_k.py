"""
since it is sequence of K,
we can do 2 pointer appraoch.

[1,2,1,3,0,1,2,2,3,1] k = 3
                   i
 [1,2,3,2,1] k = 3

 defaultDict and prefix sum
 in the single loop
 we go through and build the prefix sum

 the intuition is that we cannot use sliding window because the charactristic of number vs. strings
 are different. Number can be add subtract later on down the list and still can be formed subsequence
 whereelse, in string that is not the case

"""
from typing import List
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        idx_sum = defaultdict(int)
        idx_sum[0] = 1

        count = 0
        pre_fix_sum = 0
        for i in range(len(nums)):
            pre_fix_sum += nums[i]
            count += idx_sum[pre_fix_sum - k]
            idx_sum[pre_fix_sum] += 1
        
        return count
    

if __name__ == '__main__':
    sol = Solution()

    val = sol.subarraySum([1,1,1], k = 2)
    print (f'value should be 2: ' + str(val))

    val = sol.subarraySum([1,2,3], k = 3)
    print(f'value should be 2: ' + str(val))
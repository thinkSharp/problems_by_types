"""
calculate the prefix sum of the given array
then have a nested loop to look for subrrays of sum equal to K

Time complexity O(n^2) where n is len of nums
space complexity O(n) where n is len of nums for saving prefix sum
"""
from collections import defaultdict
class Solution:
    def subarraySum_nsquare(self, nums: list[int], k: int) -> list[list[int]]:
        n = len(nums)
        if n == 0:
            return []
        
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        result = []
        for i in range(n + 1):
            for j in range(i, n + 1):
                if prefix_sum[j] - prefix_sum[i] == k:
                    result.append(nums[i: j + 1])
        return result
    
    def subarraySum(self, nums: list[int], k: int) -> int:
        count, sum_ = 0, 0
        prefix = {0: 1}
        for num in nums:
            sum_ += num
            if sum_ - k in prefix:
                count += prefix[sum_ - k]
            prefix[sum_] += 1
        return count
    
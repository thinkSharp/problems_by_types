"""
longest increasing subsequence can be found using dynamic programming

- with bottom up approach with loop
- optimize bottom up approach if we can
"""
class Solution:
    def longest_increasing_subseuence(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    

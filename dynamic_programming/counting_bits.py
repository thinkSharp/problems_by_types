"""
Counting bit can be solved using dynamic programming
1. identify the recurrent relationship
    for any given number. we can get the calculation from i //2 +  remainder
2. based cases 0 == 0 1 == 1
3. recursive function
"""
class Solution:
    def count_bits_plain(self, n: int):
        # Your code goes here

        def count_helper(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            return count_helper(n//2) + n % 2

        result = []
        for i in range(n + 1):
            result.append(count_helper(i))
        return result

    def count_bits_with_memo(self, n: int):
        memo = {}
        def count_helper(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = count_helper(n // 2) + (n % 2)
            return memo[n]
        result = []
        for i in range(n + 1):
            result.append(count_helper(i))
        return result
    
    def count_bits(self, n: int):
        if n == 0:
            return [0]

        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i // 2] + (i % 2)
        result = []
        for i in range(n + 1):
            result.append(dp[i])
        return result
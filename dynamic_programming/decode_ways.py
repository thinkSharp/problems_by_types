"""
dyanmic programming 
1. recurrant relationship:
    can calculate one and pass on the rest to recursive function
    can calculate two and pass on the rest to recursive function
2. base:
    i ==  0 False
    i > 0 and i < 27 True else False
3. Recursive
4. Recursive function with memo
5. Bottom up approach
6. Optimize bottom up approch
"""
class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)

        if n > 0 and s[0] == '0':
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            one = int(s[i - 1])
            two = int(s[i - 2: i])

            if 1 <= one <= 9:
                dp[i] += dp[i - 1]
            if 10 <= two <= 26:
                dp[i] += dp[i - 2]
        return dp[n]

    def numDecodings_memo(self, s: str) -> int:
        if len(s) == 0:
            return 0
        memo = {}

        def decode_helper(rest, count):

            if len(rest) >= 1 and rest[0] == '0':
                return 0
            if len(rest) == 0:
                count += 1
                return count

            if rest in memo:
                return memo[rest]

            curr = rest[:1]
            one, two = 0, 0
            if len(rest) > 1 and 1 <= int(curr) <= 9:
                one = decode_helper(rest[1:], count)

            curr = rest[:2]
            if 1 <= int(curr) <= 26:
                two = decode_helper(rest[2:], count)

            memo[rest] = one + two
            return memo[rest]

        count = decode_helper(s, 0)
        return count

    def numDecodings_generic(self, s: str) -> int:
        if len(s) == 0:
            return 0

        count = 0

        def decode_helper(rest):
            nonlocal count

            if len(rest) >= 1 and rest[0] == '0':
                return
            if len(rest) == 0:
                count += 1
                return

            curr = rest[:1]
            if len(rest) > 1 and 1 <= int(curr) <= 9:
                decode_helper(rest[1:])

            curr = rest[:2]
            if 1 <= int(curr) <= 26:
                decode_helper(rest[2:])

        decode_helper(s)
        return count

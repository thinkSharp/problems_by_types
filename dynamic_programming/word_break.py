"""
In order to find the word break
use dynamic programming
initialize dp [False] * ( n  + 1)
for length of s start from index 1
loop through the words to to if fit,
then update dp 
return last dp
"""
class Solution:
    def wordBreak(s: str, worddict: list[str]) -> bool:
        n = len(s)
        if n == 0:
            return False
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for word in worddict:
                if i >= len(word) and dp[i - len(word)]:
                    sub = s[i - len(word): i]
                    if sub == word:
                        dp[i] = True
                        break

        return dp[len(s)]
    
"""
Generate parentheses can be done using back tracking 
in simplify version, just build string on the fly and check left and right paren
"""
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return []
        result = []

        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                result.append(s)
                return
            
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
        
        backtrack()
        return result
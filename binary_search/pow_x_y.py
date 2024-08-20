"""
building a pow function for a given x, n:

few tricks for optimization

with recursive functions, call pow by dividing the n // 2
handle modulo case separately
return calculated value
"""
class Solution:
    def myPowRecursive(self, x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        half = self.myPowRecursive(x, n // 2)
        res = half * half

        if n % 2 == 1:
            res = res * x

        return res
    
    def myPow(self, x, n) -> int:
        answer = self.myPowRecursive(x, abs(n))

        if n < 0:
            return 1 / answer
        return answer
    
    
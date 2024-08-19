"""
in order to multiply string.
- convert string to int 
- individually build integer from right to left
- once we have integer find the smallest one
- add large time smallest time
- finally check the sign of both integer
- if one of them is negative, output should be negative as well
"""
class Solution:
    def toInt(self, num: str) -> int:
        val = 0
        digit = {'0':0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        multiplier = [1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]
        idx = 0
        for i in range(len(num) -1, -1, -1):
            s = num[i]
            if s == '-' or s == '+':
                break
            
            d = digit[s]
            multi = multiplier[idx]
            for _ in range(d):
                val += multi
            idx += 1

        if num[0] == '-':
            val = -val
        
        return val
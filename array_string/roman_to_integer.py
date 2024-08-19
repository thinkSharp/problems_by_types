"""
convert romain to integer
idea to have declare roman representation
loop through from the back.
one trick to consider is look agead if it is VLD 
return the number

III
i

MCMXCIV
i

res += 5
res -= 5
res += 4
res += 100
res -= 100
res += 90
res += 1000
res -= 1000
res += 900
res += 1000
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        result = symbol[s[len(s) - 1]]
        idx = len(s) - 2

        while idx >= 0:
            chr = s[idx]
            prev = s[idx + 1]
            if chr + prev in symbol:
                result -= symbol[prev]
                result += symbol[chr + prev]
            else:
                result += symbol[chr]
            idx -= 1
        
        return result
    

if __name__ == '__main__':
    sol = Solution()

    assert(sol.romanToInt('III')) == 3
    assert(sol.romanToInt('LVIII')) == 58
    assert(sol.romanToInt('MCMXCIV')) == 1994
    print('romain to int')

    




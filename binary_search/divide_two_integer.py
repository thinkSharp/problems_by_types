"""
dividend and divisor without using multiplication or division or mod operation

that means only add or subtract
we should be able to substract divisor from divident until it is less than divisor
ignore decimal
special handling of negative no.

Example: 10 by 3
while dividend >= divsor:
  quoent +=
  divident -= divisor

  -7 by 2
  
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        answer = 0
        negative = 0

        if dividend < 0:
            dividend = -dividend
            negative += 1
        if divisor < 0:
            divisor = -divisor
            negative += 1

        if divisor == 1:
            answer = dividend
        else:
            while dividend >= divisor:
                answer += 1
                dividend -= divisor

        if negative == 1:
            answer = -answer
        
        return answer
    

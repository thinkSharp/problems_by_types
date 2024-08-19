"""
convert string to integer: make sure all the leading white spaces are ignore. intermediate whilte 
spaces are ignore and all ther no digit char stop
round the outof bound numeric val to -2^31 and 2^31 - 1 for positive 

Implementation Plan:
- strip white spaces both ends
- special check for sign on first char and store it
- loop through remaining and stop until none digit encountered
- conver the read in char to num
- round to - 2^31 o 2 ^31 - 1

isdigit
define int_max, int_min constant


"""
class Solution:
    def myAtoi(self, s: str):
        s = s.strip()
        if len(s) == 0:
            return 0
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        str_digit, result, start = [], 0, 0


        if s[0] == '-' or s[0] == '+':
            str_digit.append(s[0])
            start = 1

        while start < len(s):
            if s[start].isdigit():
                str_digit.append(s[start])
                start += 1
            else:
                break

        if len(str_digit) == 1 and (str_digit[0] == '+' or str_digit[0] == '-'):
            str_digit.pop(0)
        
        if len(str_digit) > 0:
            result = int(''.join(str_digit))

        if result > INT_MAX:
            result = INT_MAX
        elif result < INT_MIN:
            result = INT_MIN

        return result
    

if __name__ == '__main__':
    sol = Solution()

    assert(sol.myAtoi('')) == 0
    assert(sol.myAtoi(' ')) == 0
    assert(sol.myAtoi('-           ')) == 0
    assert(sol.myAtoi('-345.345')) == -345
    assert(sol.myAtoi(';adfadf1234')) == 0
    assert(sol.myAtoi('12345')) == 12345
    



        





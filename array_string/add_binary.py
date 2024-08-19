"""
we have to add letter from right to left, 
- one thing to keep in mind is that we need to worry about carry
- 1 + 1 => 10 
- 1 + 0 or 0 + 1 = 1

Example  '11' , '1'

0 0 1 => '100'

a ='1010' b ='1011'

1 0 1 0 1 => '10101'


"""
class Solution:
    def addBinary2(self, a:str, b:str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]
    
    def addBinary(self, a:str, b:str) -> str:
        a_p, b_p = len(a) - 1, len(b) - 1

        carry = 0
        result = []
        while a_p >= 0 or b_p >= 0:
            
            add_val =  carry
            if a_p >= 0:
                add_val += int(a[a_p])
                a_p -= 1
            if b_p >= 0:
                add_val += int(b[b_p])
                b_p -= 1

            carry = 1 if add_val > 1 else 0
            if add_val == 2 or add_val == 0:
                result.append('0')
            else:
                result.append('1')
        if carry == 1:
            result.append('1')
        
        return ''.join(result[::-1])
    

if __name__ == '__main__':
    sol = Solution()

    print(sol.addBinary('11', '1'))
    print(sol.addBinary('1010', '1011'))
    print(sol.addBinary('10111', '1011001'))

    print(sol.addBinary2('11', '1'))
    print(sol.addBinary2('1010', '1011'))
    print(sol.addBinary2('10111', '1011001'))


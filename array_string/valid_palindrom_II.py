"""
check for valid Palindrom II by removing at most one char
approach is to compare left and right pointers 
if miss match found:
    compare rest by ignoring left and right
    if either one of them return true, return true
return True
Time complexity : O(n)

aba
 l 
 r

abca
 l
 r

acdbbddca
   l
     r
"""
class Solution:
    def validPalindrom_internal(self, s: str, first_check: bool) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                if not first_check:
                    return False
                left_check = self.validPalindrom_internal(s[left + 1: right + 1], False) 
                right_check = self.validPalindrom_internal(s[left: right], False) 
                return left_check or right_check
            left += 1
            right -= 1

        return True
    
    def validPalindrom(self, s: str) -> bool:
        return self.validPalindrom_internal(s, True)
    

if __name__ == '__main__':
    sol = Solution()
    assert(sol.validPalindrom('deeee')) == True
    assert(sol.validPalindrom('aba')) == True
    assert(sol.validPalindrom('abca')) == True
    assert(sol.validPalindrom('abc')) == False
    assert(sol.validPalindrom('acdbbddca')) == True
    print('Hello World')

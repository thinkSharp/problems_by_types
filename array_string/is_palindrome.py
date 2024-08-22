"""

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = s.strip()
        if len(s) == 0:
            return True

        left, right = 0, len(s) - 1
        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True
        
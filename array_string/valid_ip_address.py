"""
IPv4
  must have 4 parts, 3 dots
  numbers must be between 0 - 255 inclusive
  leading zeros are not allow
  
IPv6
  must have 8 parts, 7 ":"
  must be hexadecimal and must have less then 4 chars
  
"""
class Solution:
    def isIPv4(self, queryIP: str) -> bool:
        parts = queryIP.split('.')
        if len(parts) != 4:
            return False
        all_digits = all(w.isdigit() for w in parts)
        if not all_digits:
            return False
        for digit in parts:
            if len(digit) > 1 and digit[0] == '0':
                return False
            val = int(digit)
            if val < 0 or val > 255:
                return False
        return True
    
    def isIPv6(self, queryIP: str) -> bool:
        parts = queryIP.split(':')
        if len(parts) != 8:
            return False
        
        return all(self.isHex(w) and len(w) > 0 and len(w) <= 4 for w in parts)
        
    def isHex(self, word: str) -> bool:
        hax_val = set('0123456789abcdefABCDEF')
        return all(c in hax_val for c in word)
        
    def validIPAddress(self, queryIP: str) -> str:
        if len(queryIP) == 0:
            return 'Neither'
        
        if self.isIPv4(queryIP):
            return 'IPv4'
        
        if self.isIPv6(queryIP):
            return 'IPv6'
        
        return 'Neither'
"""
In order to be one edit away,
s and t must be either equal distance or one distance apart
in order to make it even more simple:
always make sure that len(s) < len(t)
  if not reverse the string 
  if dif between two strings are greater then 1 then return false
  other wise loop through the small string:
    if first unmatch found:
        compare the length:
        if same then rest must much
        if different then i ==i + 1
        
  if came out of the loop
  return true if s_1 == t
  
  bab abb
 
"""

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        slen, tlen = len(s), len(t)
        
        if slen > tlen:
            return self.isOneEditDistance(t, s)
        
        if tlen - slen > 1:
            return False
        
        for i in range(slen):
            if s[i] != t[i]:
                if slen == tlen:
                    return s[i + 1:]  == t[i + 1:]
            
                else:
                    return s[i:] == t[i + 1:]
                
        return slen + 1 == tlen
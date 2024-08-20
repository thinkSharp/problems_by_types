""""
Finding the first bad version of the release. If one version is bad all version is bad.
perform binary search to get to the first bad version

the condition is to check if isbadversion,
if true then we know the first one could be at the left, so move the right
else move left
return left
"""

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return True

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left , right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            
            bad_version = isBadVersion(mid)
            if bad_version:
                right = mid - 1
            else:
                left = mid + 1
        return left
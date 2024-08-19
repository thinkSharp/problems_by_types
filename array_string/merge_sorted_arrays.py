"""
merge sorted array in place
nums1 has extra zeros space to accomodate nums2
nums1 = [1, 2, 2, 3, 5, 6] , nums2 = [0, 0, 0]
            l        
               z
                                    r
[1, 2, 2, 3, 4, 4, 6, 8] [0, 0, 0]
    z
    l
                    r   
"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n :int) -> None:
        if n == 0:
            return None

        z = len(nums1) - 1
        left = m - 1
        right = n - 1

        while right >= 0 and left >= 0:
            if nums1[left] > nums2[right]:
                nums1[left], nums1[z] = nums1[z], nums1[left]
                left -= 1
                z -= 1
            else:
                nums2[right], nums1[z] = nums1[z], nums2[right]
                right -= 1
                z -= 1

        while right >= 0:
            nums2[right], nums1[z] = nums1[z], nums2[right]
            right -= 1
            z -= 1


if __name__ == '__main__':
    sol = Solution()

    sol.merge([4,5,6,0,0,0], 3, [1,2,3], 3)


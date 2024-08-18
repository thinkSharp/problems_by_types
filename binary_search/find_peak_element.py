import unittest
"""
finding Peak elememnt is look for an element in the sorted array such that i - 1 < i > i + 1 and 
edge cases mid == 0 then i > i + 1 and mid == len(nums) - 1 then i < i - 1 => returning mid

in another words, if I simplify this condition and loop only when left < right, and check if mid > m+ 1
if that condition mat, move right = mid, else: move left = mid + 1. return left

Example:
    m
        l
        r
[1, 3, 20, 4, 5] peak
       m
          m
             l
             r 
[1, 2, 3, 4, 6]
Simplified approach does not work for this given scenario for simplified peak finding
we will have to use above approach
So let's build both appraoch
"""
def fine_peak_simplified(nums):
    ln = len(nums) 
    if ln < 2:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[-1] > nums[-2]:
        return ln - 1
    
    left, right = 1, len(nums) - 2
    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
            return mid
        elif nums[mid] < nums[mid - 1]:
            right = mid - 1
        elif nums[mid] < nums[mid + 1]:
            left = mid + 1

        return - 1



        
         
    

        

if __name__ == "__main__":
    """
          m
     l        r
    [1,3,30,4,5] 
     
              m
                 l
                 r
    [1, 3, 4, 5, 6]
    """
    assert(fine_peak_simplified([1,3,20,4,2])) == 2
    assert(fine_peak_simplified([1,20,3,2,1])) == 1
    assert(fine_peak_simplified([1,2,3,4,6])) == 4
    assert(fine_peak_simplified([20,1,2,3,4,5])) == 0
    


import unittest
"""
This is just basica binary search:
function must return target value in the sorted array within O(logn) time
cases:
   r  
   l
   m    
[1, 3, 5, 7, 9] , target = 3 => mid = (left + right) // 2
                  while left <= right:
"""
def basic_binary_search(nums, target) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == '__main__':
    """
        m
        l
        r
    #[1,3,5,7,9] target = 3

                 m
                    l
                 r
    [2, 4, 6 ,8, 10] target = 11
    """
    assert(basic_binary_search([1, 3, 5 ,7, 9], 3)) == 1
    assert(basic_binary_search([], 0)) == -1
    assert(basic_binary_search([2, 4, 6, 8, 10], 12)) == -1
    assert(basic_binary_search([1, 3, 5, 7], -2)) == -1
    
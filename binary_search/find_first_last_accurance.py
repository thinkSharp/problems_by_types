import unittest
"""
finding first and last accurance of binary search is basically find the range of element from the sorted 
binary search
- idea is to search twice,
- first get the left element for the range
- second get the right element for the range
Example:
          l     
          r
          m
[2, 4, 4, 4, 6, 8] , 4

       l           
    r
    m
[1, 3, 5, 7, 9] , 4
"""
def find_edge_binary_search(nums, target, left_direction):
    result, left, right = -1, 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            result = mid
            if left_direction:
                right = mid - 1
            else:
                left = mid + 1
    return result

def find_first_last_accurance_binary_search(nums, target):
    if len(nums) == 0:
        return [-1, -1]
    
    left = find_edge_binary_search(nums, target, True)
    right = find_edge_binary_search(nums, target, False)

    return [left, right]


if __name__ == "__main__":

    assert(find_first_last_accurance_binary_search([1, 2, 4 , 4, 4, 5, 6, 7], 4)) == [2, 4]
    assert(find_first_last_accurance_binary_search([1, 2, 4 , 4, 4, 5, 6, 7], 5)) == [5, 5]
    assert(find_first_last_accurance_binary_search([1, 2], 4)) == [-1, -1]
    assert(find_first_last_accurance_binary_search([2, 2, 2, 2], 2)) == [0, 3] 

"""
finding peak in rotated array
          m
          l
          r
[3, 4, 5, 1, 2]
       m
         l
         r
[2,3,4,5,1]
         m
         l
         r  
[1,2,3,4,5]
     m
     l 
     r
[7,6,1,2,3,4,5]
"""
def find_peak_rotated_sorted_array(nums):
    if len(nums) == 0:
        return -1
    
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    if left == right == mid == 0:
        return len(nums) - 1
    
    return left - 1 if left > 0  else left
    

if __name__ == '__main__':
    assert(find_peak_rotated_sorted_array([3,4,5,1,2])) == 2
    assert(find_peak_rotated_sorted_array([2,3,4,5,1])) == 3
    assert(find_peak_rotated_sorted_array([1,2,3,4,5])) == 4
    assert(find_peak_rotated_sorted_array([])) == -1
    assert(find_peak_rotated_sorted_array([1,2])) == 1
    assert(find_peak_rotated_sorted_array([7,6,1,2,3,4,5])) == 1
    print("hello World")

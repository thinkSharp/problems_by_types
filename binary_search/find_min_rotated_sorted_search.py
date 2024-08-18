"""
finding minimum in rotated such is similar to find peak in rotated suearch
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
[6,5,1,2,3,4]
"""
def find_min_rotated_sorted_array(nums):
    if len(nums) == 0:
        return -1
    
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid


    return left
    

if __name__ == '__main__':
    assert(find_min_rotated_sorted_array([3,4,5,1,2])) == 3
    assert(find_min_rotated_sorted_array([2,3,4,5,1])) == 4
    assert(find_min_rotated_sorted_array([1,2,3,4,5])) == 0
    assert(find_min_rotated_sorted_array([])) == -1
    assert(find_min_rotated_sorted_array([1,2])) == 0
    assert(find_min_rotated_sorted_array([6,5,1,2,3,4])) == 2


    print("hello World")

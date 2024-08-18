"""
similar to peak, find any dip element in the array
[1,2,0,4,5,6,7] it should return 0
the check is to make sure mid < mid - 1. 

 
[1,2,3,4,5] => 1
[4,2,3,4,5,0] => 0 or 2
       m
     l    
     r
[2,2,-1,3,4] => -1
        m
        l
      r
[1,2,-1,7,8,4,5] => -1 or 4


"""
def find_dip(nums):
    ln = len(nums)
    if ln < 2:
        return 0
    
    if nums[0] < nums[1]:
        return 0
    if nums[-1] < nums[-2]:
        return ln - 1
    
    left , right = 1, ln - 2
    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
            return mid
        elif nums[mid] > nums[mid - 1]:
            right = mid - 1
        elif nums[mid] > nums[mid + 1]:
            left = mid + 1
            
    return -1

if __name__ == '__main__':
    assert(find_dip([3,2,-1,7,8,4,5])) == 2
    """ 
                      m
                      l     
                      r  
    """
    assert(find_dip([4,2,3,4,5,6])) == 1
    assert(find_dip([1,2,3,4,5])) == 0
    assert(find_dip([3,2,3,4,3])) == 4 

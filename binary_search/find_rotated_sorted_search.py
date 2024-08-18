"""
find target of the rotated sort:
example:
                 m
                   l               
                 r
[4,5,6,7,0,1,1,2,3], target is 5

divide and check the mid if equal to target return
otherwise, mid >= left
mid 
"""
def find_rotated_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        elif nums[mid] >= nums[left]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
    return -1



"""

 l           r
       m
[6,7,1,2,3,4,5] , t = 6
       m
 l               
       r
[4,5,6,7,0,1,1,2,3], target is 5

[1,2], target is 1
       l r
         m
[0,1,2,3,4] target is 4

[5,1,2,3,4] target is 5

"""
if __name__ == '__main__':
    
    #val = find_rotated_search([1,2], 1)
    #print(val)
    #print(val == 0)
    val = find_rotated_search([6,7,0,1,1,2,3,4,5], 6)
    print(val)
    val = find_rotated_search([4,5,6,7,0,1,1,2,3], 4)
    print(val)

    #assert(find_rotated_search([0,1,2,3,4], 4)) == 4
    #assert(find_rotated_search([6,7,1,2,3,4,5], 6)) == 0

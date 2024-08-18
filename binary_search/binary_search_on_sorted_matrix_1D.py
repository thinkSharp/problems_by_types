"""
this is binary search on sorted matrix using 1D array representation
in this approach: we will calculate total len of array by n * m
search binary normally.
when comparing, we will convert mid to mid_r, mid_c
the formula for mid_r = mid // m and mid_c = mid % m 

"""

def search_target_in_sorted_grid(grid, target):
    row_l = len(grid)
    if row_l == 0:
        return -1, -1
    
    col_l = len(grid[0])

    left , right = 0, (row_l * col_l) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_r, mid_c = mid // col_l, mid % col_l
        if grid[mid_r][mid_c] == target:
            return mid_r, mid_c
        
        elif target > grid[mid_r][mid_c]:
            left = mid + 1
        else:
            right = mid - 1

    return -1, -1


"""
[ [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9]]
"""
if __name__ == '__main__':
    grid1 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
    val = search_target_in_sorted_grid(grid1, 9)
    print(val)
    grid2 = [
  [7, 7, 7],
  [7, 7, 7],
  [7, 7, 7]
]
    val = search_target_in_sorted_grid(grid2, 7)
    print(val)

    grid3 = [
  [1,   2,  3,  4,  5],
  [10, 20, 30, 40, 50],
  [100,200,300,400,500]
]
    val = search_target_in_sorted_grid(grid3, 400)
    print(val)

    grid4 = [  [-50, -40, -30, -20],
  [-10,  -5,   0,   5],
  [ 10,  20,  30,  40],
  [ 50,  60,  70,  80]
]
    val = search_target_in_sorted_grid(grid4, -30)
    print(val)

    val = search_target_in_sorted_grid(grid4, -300)
    print(val)



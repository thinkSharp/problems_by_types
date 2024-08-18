"""
In order to find the target element in sorted grid,
we need to perform row search and then column search
for row search:
row 0 to n:
  if target > first and less then last:
    break
  elif first > target b = mid - 1
  else top = mid + 1


once we find the row index
search column should be normal affair

Time complexity should be O(log n + log m)
"""
def search_row_index(grid, target):
    top, bottom = 0, len(grid) - 1
    while top <= bottom:
        mid = (top + bottom) // 2

        if grid[mid][0] <= target <= grid[mid][-1]:
            return mid
        elif grid[mid][0] > target:
            bottom = mid - 1
        else:
            top = mid + 1
    return -1

def search_target_in_sorted_grid(grid, target):
    row_l = len(grid)
    if row_l == 0:
        return -1, -1
    
    col_l = len(grid[0])

    target_row = search_row_index(grid, target)

    if target_row == -1:
        return -1, -1
    
    left, right = 0, col_l - 1
    while left <= right:
        mid = (left + right) // 2
        if grid[target_row][mid] == target:
            return target_row, mid
        
        elif target > grid[target_row][mid]:
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



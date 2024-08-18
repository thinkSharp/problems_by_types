"""
definition: Peak in a grid:
a cell is consider peak when left, right, top, bottom are all less then or equal to the cell
there can be several peak in the grid.
We are not looking for global minimum. Just any peak

Strategy: Gready approach
first pick max val from a row. let say middle row
check if it is peak, if it is then return,
if not move to the largest element in the neighbor continue there
either you will find the peak or largest element and go from there
"""
def check_neighbor(grid, peak, row, col, check):
    max_neighbor, max_point = check
    found = True
    if grid[row][col] > peak:
        found = False
        if grid[row][col] > max_neighbor:
            max_neighbor = grid[row][col]
            max_point = row, col
    return found, max_neighbor, max_point

def is_peak(grid, peak):
    row_count, col_count = len(grid) - 1, len(grid[0]) - 1
    max_neighbor = float('-inf')
    max_points = None
    row, col = peak
    peak_val = grid[row][col]
    found = True
    if col > 0:
        found, max_neighbor, max_points = check_neighbor(grid, peak_val, row, col - 1, (max_neighbor, max_points))
    if col < col_count:
        found, max_neighbor, max_points = check_neighbor(grid, peak_val, row, col + 1, (max_neighbor, max_points))
    if row > 0:
        found, max_neighbor, max_points = check_neighbor(grid, peak_val, row - 0, col, (max_neighbor, max_points))
    if row < row_count:
        found, max_neighbor, max_points = check_neighbor(grid, peak_val, row + 1, col, (max_neighbor, max_points))

    return found, max_points, max_neighbor
    
    
def find_a_peak_in_a_grid(grid):
    row_count = len(grid)
    if row_count == 0:
        return -1, -1
    
    mid = row_count // 2

    col_count = len(grid[0])

    peak = None
    max_peak = float('-inf')
    for c in range(col_count):
        if grid[mid][c] > max_peak:
            max_peak = grid[mid][c]
            peak = (mid, c)

    found = False   
    while not found:
         print(peak)
         found, new_peak, new_max = is_peak(grid, peak)
         if found:
             return peak
         peak = new_peak
         max_peak = new_max
         
    return -1, -1


if __name__ == '__main__':
    grid = [  
  [10, 13, 15, 17],
  [ 9, 11, 16, 19],
  [ 8, 12, 14, 20],
  [ 7, 18, 21, 22]
]
    point = find_a_peak_in_a_grid(grid)
    print(point)
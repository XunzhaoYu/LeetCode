"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:
    Input:
        [[0,1,0,0],
         [1,1,1,0],
         [0,1,0,0],
         [1,1,0,0]]

    Output: 16

    Explanation: The perimeter is the 16 yellow stripes in the image below:
"""


def islandPerimeter(grid: List[List[int]]) -> int:
    # 144 ms, faster than 99.49%.
    rows, cols, ans = len(grid), len(grid[0]), 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                ans += 4
                if r + 1 < rows and grid[r + 1][c] == 1:
                    ans -= 2
                if c + 1 < cols and grid[r][c + 1] == 1:
                    ans -= 2
    return ans


def islandPerimeter2(grid: List[List[int]]) -> int:
    # 136 ms, faster than 99.61%. The best solution from submissions (132 ms).
    ans = 0
    for row,row_val in enumerate(grid):  # ***
        for column,column_val in enumerate(row_val):
            if column_val:
                ans += 4
                # check if there is a grid above
                if row > 0 and grid[row-1][column]: ans -= 2
                #check if there is adjacent grid before
                if column > 0 and grid[row][column-1]: ans -= 2
    return ans

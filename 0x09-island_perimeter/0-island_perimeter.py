#!/usr/bin/python3
"""Island Perimeter"""

def island_perimeter(grid):
    """
    Calculates the Perimeter of an isand.
    Parameters:
        - grid: 2d matrix
    Returns:
        -perimeter(int)
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 2
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -=2
    return perimeter

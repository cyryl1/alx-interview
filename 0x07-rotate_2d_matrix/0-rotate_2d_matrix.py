#!/usr/bin/python3
"""0-rotate_2d_matrix"""

def rotate_2d_matrix(matrix):
    """Rotate a square by 90 degree
    Args:
        matrix
    Returns:
        None
    """
    # Let's transpose first
    n = len(matrix)
    m = len(matrix[0])
    tr = [[matrix[j][i] for j in range(n)] for i in range(m)]

    for i in range(m):
        tr[i].reverse()
    
    for i in range(m):
        for j in range(n):
            matrix[i][j] = tr[i][j]
    
    # res = [[0] * n for _ in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         res[n - j - 1][i] = matrix[i][j]

    # for i in range(n):
    #     for j in range(n):
    #         matrix[i][j] = res[i][j]


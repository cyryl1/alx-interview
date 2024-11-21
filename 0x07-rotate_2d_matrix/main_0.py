#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    # matrix = [[10, 11, 12],
    #           [1, 4, 7, 10],
    #           [2, 5, 8, 11],
    #           [3, 6, 9, 12]]

    rotate_2d_matrix(matrix)
    for row in matrix:
        print(row)
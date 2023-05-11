#!/usr/bin/python3
"""
rotates 2d-matrix
"""


def rotate_2d_matrix(matrix):
    """
    rotates 2d-matrix
    """
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse the rows
    for i in range(n):
        matrix[i] = matrix[i][::-1]

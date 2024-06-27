#!/usr/bin/python3
"""Triangle"""


def pascal_triangle(n):
    """Pascal Triangle"""
    if n <= 0:
        return []
    x = [[1]]
    for row_num in range(1, n):
        row = [1]
        for j in range(1, row_num):
            e = x[row_num - 1][j - 1] + x[row_num - 1][j]
            row.append(e)
        row.append(1)
        x.append(row)

    return x

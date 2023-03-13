#!/usr/bin/python3
"""Module for  Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n."""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangles = [[1]]
    while len(triangles) != n:
        temp = triangles[-1]
        row = [1]
        for i in range(len(temp) - 1):
            row.append(temp[i] + temp[i + 1])
        row.append(1)
        triangles.append(row)
    return triangles

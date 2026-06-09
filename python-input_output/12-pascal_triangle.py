#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s triangle.

    Args:
        n (int): The number of rows of the triangle to generate.
    Returns:
        list: A list of lists representing Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        prev_row = triangle[-1]
        new_row = [1]
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])
        new_row.append(1)
        triangle.append(new_row)

    return triangle

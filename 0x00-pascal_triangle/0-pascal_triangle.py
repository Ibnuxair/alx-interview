#!/usr/bin/python3
"""  Contains function pascal_triangle """


def pascal_triangle(n):
    """ returns a list of lists of integers representing the Pascals

    or empty list if n <= 0
    """
    if n <= 0:
        return ([])

    pascal = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = pascal[i - 1]
        for j in range(len(prev_row)):
            new_element = prev_row[j] + prev_row[j + 1] if j != len(prev_row) - 1 else 1
            row.append(new_element)

        pascal.append(row)

    return pascal

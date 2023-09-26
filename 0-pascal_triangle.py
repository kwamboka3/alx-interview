#!/usr/bin/python3
"""
Pascal Triangle exercise file
"""


def fact(n):
    """
    A function to recursively perform the factorial
    operation on a number
    :param n:
    :return: The factorial, denoted by n! mathematically
    """
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)


def pascal_triangle(n):
    """
    Using the fact function above, we compute
    a combination using the given parameter n
    to produce the famous pascals triangle
    """
    result = []
    if n > 0:
        for i in range(n):
            new_list = []
            for j in range(i+1):
                new_list.append(int((fact(i)/(fact(i-j)*fact(j)))))
            result.append(new_list)

    return result

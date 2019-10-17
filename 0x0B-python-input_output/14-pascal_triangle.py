#!/usr/bin/python3
"""
    Begin program - python
"""


def pascal_triangle(n):
    """Begin program - python"""
    a = []
    if n <= 0:
        return a
    # for i in range(n):
    #     b = []
    #     for j in range(i + 1):
    #         b.append(int(fc(i)/(fc(j) * fc(i - j))))
    #     a.append(b)
    for i in range(n):
        b = [1]
        if a:
            for j in range(i):
                b.append(sum(a[-1][j:j+2]))
        a.append(b)
    return a

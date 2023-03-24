#!/usr/bin/python3

def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    """

    if n <= 0:
        return []

    triangle = [[1]]
    triangleIndex = 0
    for i in range(1, n):
        newLevel = [1]
        j = 0
        leng = len(triangle[triangleIndex])
        while j + 1 != leng:
            num = triangle[triangleIndex][j] + triangle[triangleIndex][j + 1]
            newLevel.append(num)
            j += 1
        newLevel.append(1)
        triangle.append(newLevel)
        triangleIndex += 1

    return triangle

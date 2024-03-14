# Problem statement
# Given an ‘N’ x ‘M’ integer matrix, if an element is 0, set its entire row and column to 0's, and return the matrix. In particular, your task is to modify it in such a way that if a cell has a value 0 (matrix[i][j] == 0), then all the cells of the ith row and jth column should be changed to 0.

# You must do it in place.

# For Example:

# If the given grid is this:
# [7, 19, 3]
# [4, 21, 0]

# Then the modified grid will be:
# [7, 19, 0]
# [0, 0,  0]
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1 :
# 2
# 2 3
# 7 19 3
# 4 21 0
# 3 3
# 1 2 3
# 4 0 6
# 7 8 9
# Sample Output 1 :
# 7 19 0
# 0 0 0
# 1 0 3
# 0 0 0
# 7 0 9
# Explanation For Sample Input 1 :
# For First Case - Similar to the example explained above.

# For Second Case -
# Only the cell (2,2) has zero. So all the elements of the second row and second column are changed to zeros.
# Sample Input 2 :
# 2
# 4 2
# 1 0
# 2 7
# 3 0
# 4 8
# 3 3
# 0 2 3
# 1 0 3
# 1 2 0
# Sample Output 2 :
# 0 0
# 2 0
# 0 0
# 4 0
# 0 0 0
# 0 0 0
# 0 0 0


# Hints:
# We can simulate the process described in the statement naively.


from math import *
from collections import *
from sys import *
from os import *

from typing import List


def setZeros(matrix: List[List[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])
    firstCol = False
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                if j == 0:
                    firstCol = True
                else:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if (matrix[0][0] == 0):
        for i in range(n):
            matrix[0][i] = 0

    if (firstCol):
        for i in range(m):
            matrix[i][0] = 0

# Problem statement
# You are given a binary matrix (it contains only 0s and 1s) with dimensions ‘N * M’. You need to find and return the sum of coverages of all zeros of the given matrix.

# Coverage for a particular 0 is defined as the total number of ‘1s’ around it (i.e., immediate left, immediate right, immediate up, and immediate bottom positions).

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 10
# 1 <= N, M <= 10^3

# Time limit: 1 second
# Sample Input 1:
# 1
# 2 2
# 1 0
# 0 1
# Sample Output 1:
# 4
# Explanation of Input 1:
# In the given matrix, there are 2 zeros.
# For the 0 at the 1st row, 2nd column position, coverage is 2(there is 1 adjacent top one and 1 adjacent right one).
# For the 0 at the 2nd row, 2nd column the coverage is 2(there is 1 adjacent top one and 1 adjacent right one).

# Hence the net coverage is 2 + 2 = 4.
# Sample Input 2:
# 1
# 2 3
# 0 0 0
# 0 0 0
# Sample Output 2
# 0

from os import *
from sys import *
from collections import *
from math import *


def coverageOfMatrix(mat):
    coverage = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if (mat[i][j] == 0):
                if (i != 0 and j != 0):
                    try:
                        coverage += mat[i-1][j]
                    except IndexError:
                        pass
                    try:
                        coverage += mat[i+1][j]
                    except IndexError:
                        pass
                    try:
                        coverage += mat[i][j-1]
                    except IndexError:
                        pass
                    try:
                        coverage += mat[i][j+1]
                    except IndexError:
                        pass
                elif (i == 0 and j == 0):
                    try:
                        coverage += mat[0][1]
                    except IndexError:
                        pass
                    try:
                        coverage += mat[1][0]
                    except IndexError:
                        pass
                elif (i == 0 and j != 0):
                    try:
                        coverage += mat[1][j]
                    except IndexError:
                        pass
                    try:
                        coverage += mat[0][j-1]
                    except IndexError:
                        pass
                    try:
                        coverage += mat[0][j+1]
                    except IndexError:
                        pass
                elif (i != 0 and j == 0):
                    try:
                        coverage += mat[i-1][0]
                    except IndexError:
                        pass
                    try:
                        coverage += mat[i][1]
                    except IndexError:
                        pass
                    try:
                        coverage += mat[i+1][j]
                    except IndexError:
                        pass
    return coverage

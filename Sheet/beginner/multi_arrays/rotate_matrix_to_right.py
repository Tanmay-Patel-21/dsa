# Problem statement
# You have been given a matrix ‘MAT’ of size 'N' * 'M' (where 'N' and 'M' denote the number of rows and columns respectively) and a positive integer ‘K’. Your task is to rotate the matrix to the right 'K' times.

# Note:
# Right rotation on a matrix is shifting each column to the right side (the last column moves to the first column) and 'K' times means performing this rotation 'K' times.
# Example:
# For 'K' = 1 and the given 'MAT':

# 1 2 3
# 4 5 6
# 7 8 9

# Output after rotating 'MAT' one time is:

# 3 1 2
# 6 4 5
# 9 7 8
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 10
# 1 <= N <= 200
# 1 <= M <= 200
# 0 <= K <= 10^9
# 1 <= MAT[i][j] <= 10^5

# Where 'MAT[i][j]' denotes the element in the 'i'th row and 'j'th column of the matrix.

# It is guaranteed that sum of 'N' * 'M' over all the test cases does not exceed 10 ^ 5.

# Time limit: 1 sec
# Sample Input 1 :
# 2
# 3 3 2
# 10 20 30
# 40 50 60
# 70 80 90
# 2 2 2
# 1 2
# 3 4
# Sample Output 1 :
# 20 30 10 50 60 40 80 90 70
# 1 2 3 4
# Explanation for Sample Output 1:
# In test case 1, Performing right rotation for the first time ('K' = 1) we get:

# 30 10 20
# 60 40 50
# 90 70 80

# Performing right rotation for the second time ('K' = 2) we get:

# 20 30 10
# 50 60 40
# 80 90 70

# The matrix after rotations will be printed in a single line row-wise. Therefore, the output is:

# 20 30 10 50 60 40 80 90 70

# In test case 2, Performing right rotation for the first time ('K' = 1) we get:

# 2 1
# 4 3

# Performing right rotation for the second time ('K' = 2) we get:

# 1 2
# 3 4

# The matrix after rotations will be printed in a single line row-wise. Therefore, the output is:

# 1 2 3 4
# Sample Input 2 :
# 2
# 2 3 2
# 1 2 3
# 4 5 6
# 4 4 1
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# Sample Output 2 :
# 2 3 1 5 6 4
# 4 1 2 3 8 5 6 7 12 9 10 11 16 13 14 15
# Explanation for Sample Output 2:
# In test case 1, Performing right rotation for the first time ('K' = 1) we get:

# 3 1 2
# 6 4 5

# Performing right rotation for the second time ('K' = 2) we get:

# 2 3 1
# 5 6 4

# The matrix after rotations will be printed in a single line row-wise. Therefore, the output is:

# 2 3 1 5 6 4

# In test case 2, Performing right rotation for the first time ('K' = 1) we get:

# 4 1 2 3
# 8 5 6 7
# 12 9 10 11
# 16 13 14 15

# The matrix after rotations will be printed in a single line row-wise. Therefore, the output is:

# 4 1 2 3 8 5 6 7 12 9 10 11 16 13 14 15

import sys
from sys import setrecursionlimit

setrecursionlimit(10**7)


def rotateMatRight(mat, n, m, k):
    k = k % m
    if k > 0:
        for row in mat:
            i = m - k
            j = m - 1
            while i < j:
                temp = row[i]
                row[i] = row[j]
                row[j] = temp
                i += 1
                j -= 1
            i = 0
            j = m - k - 1
            while i < j:
                temp = row[i]
                row[i] = row[j]
                row[j] = temp
                i += 1
                j -= 1
            i = 0
            j = m - 1
            while i < j:
                temp = row[i]
                row[i] = row[j]
                row[j] = temp
                i += 1
                j -= 1
    return mat


def takeInput():
    n, m, k = map(int, input().strip().split(" "))
    mat = [list(map(int, input().strip().split(" "))) for row in range(n)]
    return n, m, k, mat


def flattenMat(mat):
    return ' '.join(map(str, [elem for row in mat for elem in row]))


# Main.
t = int(input().strip())
for i in range(t):
    n, m, k, mat = takeInput()
    mat = rotateMatRight(mat, n, m, k)
    print(flattenMat(mat))

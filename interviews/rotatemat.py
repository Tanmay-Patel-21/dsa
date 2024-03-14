import sys
from sys import setrecursionlimit

setrecursionlimit(10**7)


def rotateMatRight(mat, n, m, k):
    k = k % m
    print(k)
    if k > 0:
        for row in mat:
            i = 0
            j = m - k - 1
            while i < j:
                temp = row[i]
                row[i] = row[j]
                row[j] = temp
                i += 1
                j -= 1
            i = m - k
            j = m - 1
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


# Main.
t = int(input().strip())
for i in range(t):
    n, m, k, mat = takeInput()
    mat = rotateMatRight(mat, n, m, k)
    print(mat)

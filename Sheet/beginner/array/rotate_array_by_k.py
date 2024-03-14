# Problem statement
# Given an array 'arr' with 'n' elements, the task is to rotate the array to the left by 'k' steps, where 'k' is non-negative.


# Example:
# 'arr '= [1,2,3,4,5]
# 'k' = 1  rotated array = [2,3,4,5,1]
# 'k' = 2  rotated array = [3,4,5,1,2]
# 'k' = 3  rotated array = [4,5,1,2,3] and so on.

from os import *
from sys import *
from collections import *
from math import *


def rotateArray(arr_len, arr, r):
    ans = []
    for i in range(arr_len):
        ans.append(arr[(i+r) % arr_len].rstrip('\r'))

    return ' '.join(ans)


arr_len = int(input())
arr = list(input().split(" "))
r = int(input())

rotatedArray = rotateArray(arr_len, arr, r)

print(rotatedArray)

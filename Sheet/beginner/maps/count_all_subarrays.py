# Problem statement
# Given an array ‘ARR’ and an integer ‘K’, your task is to find all the count of all sub-arrays whose sum is divisible by the given integer ‘K’.

# Note:
# If there exists no subarray in the given sequence whose sum is divisible by ‘K’ then simply return ‘0’.
# Example:
# Suppose the given array is ‘ARR’ = { 5, 0, 2, 3, 1} and ‘K = 5’.
# As we can see in below image, there are a total of 6 subarrays that have the total sum divisible by ‘K’
# So we return the integer 6.

from os import *
from sys import *
from collections import *
from math import *


def subArrayCount(arr, k):
    ans = 0
    remCount = {}
    remCount[0] = 1
    mySum = 0
    myRem = 0
    for i in arr:
        mySum += i
        myRem = mySum % k

        if myRem < 0:
            myRem += k

        if myRem in remCount.keys():
            ans += remCount[myRem]
            remCount[myRem] = remCount[myRem]+1
        else:
            remCount[myRem] = 1

    return ans

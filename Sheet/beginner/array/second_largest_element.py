# Problem statement
# You have been given an array/list 'ARR' of integers. Your task is to find the second largest element present in the 'ARR'.

# Note:
# a) Duplicate elements may be present.

# b) If no such element is present return -1.
# Example:
# Input: Given a sequence of five numbers 2, 4, 5, 6, 8.

# Output:  6

# Explanation:
# In the given sequence of numbers, number 8 is the largest element, followed by number 6 which is the second-largest element. Hence we return number 6 which is the second-largest element in the sequence.

from os import *
from sys import *
from collections import *
from math import *


def findSecondLargest(sequenceOfNumbers):
    # Write your code here.
    sequenceOfNumbers.sort(reverse=True)
    i = 0
    while (i < len(sequenceOfNumbers)-1):
        if (sequenceOfNumbers[i] > sequenceOfNumbers[i+1]):
            return sequenceOfNumbers[i+1]

        i = i+1
    return -1
# Taking input using fast I/O.


def takeInput():
    n = int(input())

    sequenceOfNumbers = list(map(int, input().strip().split(" ")))

    return sequenceOfNumbers, n


# Main.
t = int(input())
while t:
    sequenceOfNumbers, n = takeInput()
    print(findSecondLargest(sequenceOfNumbers))
    t = t-1

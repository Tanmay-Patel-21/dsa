# Problem statement
# Given an unsorted array of integers, you have to move the array elements in a way such that all the zeroes are transferred to the end, and all the non-zero elements are moved to the front. The non-zero elements must be ordered in their order of appearance.

# For example, if the input array is: [0, 1, -2, 3, 4, 0, 5, -27, 9, 0], then the output array must be:

# [1, -2, 3, 4, 5, -27, 9, 0, 0, 0].

# Expected Complexity: Try doing it in O(n) time complexity and O(1) space complexity. Here, ‘n’ is the size of the array.

# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# 2
# 7
# 2 0 4 1 3 0 28
# 5
# 0 0 0 0 1
# Sample Output 1:
# 2 4 1 3 28 0 0
# 1 0 0 0 0
# The explanation for Sample Output 1 :
# In the first testcase, All the zeros are moved towards the end of the array, and the non-zero elements are pushed towards the left, maintaining their order with respect to the original array.

# In the second testcase, All zero are moved towards the end, hence the only non-zero element i.e 1 is in the starting of the array
# Sample Input 2:
# 2
# 5
# 0 3 0 2 0
# 4
# 0 0 0 0
# Sample Output 2:
# 3 2 0 0 0
# 0 0 0 0

def pushZerosAtEnd(arr):
    i = 0
    j = 1
    while (j < len(arr)):
        if (arr[i] == 0 and arr[j] == 0):
            j += 1
        else:
            if (arr[i] == 0):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            i += 1
            j += 1

# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).


# Example 1:

# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:

# Input: nums = [4,2,1]
# Output: false
# Explanation: You cannot get a non-decreasing array by modifying at most one element.


class Solution(object):
    def checkPossibility(self, arr):
        counter = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                if counter or (i > 1 and i < len(arr) - 1 and arr[i-2] > arr[i] and arr[i+1] < arr[i-1]):
                    return False
                counter = 1
        return True

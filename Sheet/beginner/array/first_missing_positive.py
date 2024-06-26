# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.


# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.


class Solution(object):
    def firstMissingPositive(self, nums):
        if 1 in nums:
            nums.sort()

            for i in range(len(nums)-1):
                if (nums[i] > 0):
                    if nums[i]+1 != nums[i+1] and nums[i] != nums[i+1]:
                        return nums[i]+1

            return nums[len(nums)-1]+1
        else:
            return 1

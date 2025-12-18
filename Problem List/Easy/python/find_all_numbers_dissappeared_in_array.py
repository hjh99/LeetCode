# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
 

# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        highest = len(nums)
        missing = []
        count = {}
        for index, value in enumerate(nums):
            if value not in count:
                count[value] = 1
            else:
                 count[value] += 1

        for i in range(1, highest+1):
            if i not in count:
                missing.append(i)

        return missing
        
# model soln
# using index to track missing numbers
class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] *= -1

        missing = []
        for i in range(len(nums)):
            if nums[i] > 0:
                missing.append(i + 1)

        return missing
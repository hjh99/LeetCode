# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]
 

# Constraints:

# 0 <= rowIndex <= 33

class Solution(object):
    def __init__(self):
        self.memo = {}

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1,1]

        this_line = []
        if rowIndex in self.memo:
            return self.memo[rowIndex]

        for i in range(rowIndex+1):
            if i == 0 or i == rowIndex:
                this_line.append(1)
            else:
                prev = self.getRow(rowIndex-1)

                this_line.append(prev[i-1] + prev[i])
            
        self.memo[rowIndex] = this_line
        return self.memo[rowIndex]
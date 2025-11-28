# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30

class Solution(object):
    def __init__(self):
            self.memo = {}
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 1:
            return [[1]]
        
        this_line = []
        if numRows in self.memo:
            return self.memo[numRows]

        for i in range(numRows):
            if i == 0 or i == numRows-1:
                this_line.append(1)
            else:
                this_line.append(self.generate(numRows - 1)[-1][i-1] + self.generate(numRows - 1)[-1][i])
            
        solution = [this_line]
        self.memo[numRows] = self.generate(numRows-1) + solution
        return self.memo[numRows]
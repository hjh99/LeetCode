# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string?

# Solution 1

import math

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        digit_list = list(map(str, str(x)))
        i = 0
        palindrome = True
        checks = math.floor(len(digit_list)/2)
        while i <= checks:
            if (digit_list[i] == '-'):
                palindrome = False
                break
            from_the_back = -1 - i
            if (digit_list[i] != digit_list[from_the_back]):
                palindrome = False
                break
            i += 1

        return palindrome
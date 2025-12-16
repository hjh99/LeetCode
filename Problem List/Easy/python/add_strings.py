# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"
 

# Constraints:

# 1 <= num1.length, num2.length <= 104
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0

        n1len = len(num1)
        n2len = len(num2)
        n1reverse = num1[::-1]
        n2reverse = num2[::-1]

        longest = 0
        total = ''

        if n1len > n2len:
            longest = n1len
            for i in range(n1len - n2len):
                n2reverse += '0'
        else:
            longest = n2len
            for j in range(n2len - n1len):
                n1reverse += '0'

        for k in range(longest):
            value = int(n1reverse[k]) + int(n2reverse[k])
            if carry == 1:
                value += 1
                carry = 0
            if value >= 10:
                carry = 1
                value -= 10
            total += str(value)
        
        if carry == 1:
            total += '1'


        return total[::-1]
            
        
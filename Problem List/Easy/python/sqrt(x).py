# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

# Constraints:

# 0 <= x <= 231 - 1


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<=1:
            return x
        
    
        binary_x =bin(x)[2:]
        len_x = len(binary_x)
        places = len_x//2
        if places == 0:
            return x
        approx_binary =binary_x[:-places]
        approx = int(approx_binary, 2)
        while (approx+1)**2 <= x:
            approx +=1
        while approx**2 > x:
            approx -=1
        
        if approx_binary == "":
            return 0

        return approx
        

# Review:

# Finding rough solution - approx and then adjusting it to fit the description
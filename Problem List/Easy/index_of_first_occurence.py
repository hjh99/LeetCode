# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        found = False
        found_index = -1
        len_needle = len(needle)
        if len_needle <= len(haystack):
            for index, char in enumerate(haystack):
                if (char == needle[0] and (index + len_needle) <= len(haystack)):
                    for j in range(len_needle):
                        if (haystack[index+j] != needle[j]):
                            break
                        if(j == len_needle-1):
                            found = True
                            found_index = index
                            return found_index                           
                else:
                    continue
        else:
            return found_index
        return found_index
        
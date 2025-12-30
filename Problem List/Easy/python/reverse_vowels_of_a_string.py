# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aAeEiIoOuU')
        appear = []
        appear_counter = []
        for index, i in enumerate(s):
            if i in vowels:
                appear.append(i)
                appear_counter.append(index)

        counter = 0
        list_string = list(s)
        appear.reverse()
        for index in appear_counter:
            list_string[index] = appear[counter]
            counter += 1
        
        result = "".join(list_string)
        
        return result
    

#use more sets when checking like list, as its O(1)
# You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:

# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Return true if the student is eligible for an attendance award, or false otherwise.

 

# Example 1:

# Input: s = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
# Example 2:

# Input: s = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.
 

# Constraints:

# 1 <= s.length <= 1000
# s[i] is either 'A', 'L', or 'P'.

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        late = False
        list_s = list(s)
        counter = 0
        absent = 0
        while counter <len(list_s):
            if list_s[counter] == 'L':
                if counter + 2 <len(list_s):
                    if list_s[counter+1] == 'L'  and list_s[counter+2] == 'L' :
                        return False
            if list_s[counter] == 'A':
                absent  += 1
            counter+=1

        if absent >= 2:
            return False
        return True



class Solution(object):
    def checkRecord(self, s):
        return s.count('A') < 2 and 'LLL' not in s
    
##clean and minimal
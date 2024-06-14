class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]
        maping= {'(':')','[':']','{':'}'}
        for char in s:
            if char in maping:
                stack.append(char)
            else:
                if not stack or maping[stack.pop()] != char:
                    return False
        return not stack            

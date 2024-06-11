class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        symbol = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        result = 0
        value = 0
        for i in reversed(s):
            current_value = symbol[i]
            if current_value >= value:
                result += current_value
            else:
                result -= current_value
            value = current_value
        return result
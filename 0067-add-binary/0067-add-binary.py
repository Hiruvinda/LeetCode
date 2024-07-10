class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal1 = int(a, 2)
        decimal2 = int(b, 2)
        
        decimal_sum = decimal1 + decimal2
        
        binary_sum = bin(decimal_sum)[2:]
        
        return binary_sum
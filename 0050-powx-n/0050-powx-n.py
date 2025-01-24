class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1  # Base case: x^0 = 1 for any x
        
        if n < 0:
            x = 1 / x  # Handle negative exponents
            n = -n
            
        result = 1
        current_product = x
        
        while n > 0:
            if n % 2 == 1:  # If the current power is odd
                result *= current_product
            
            current_product *= current_product  # Square the base
            n //= 2  # Reduce the power by half
        
        return result

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
           return False
        
        reverse_x = 0
        place_value= 1
        org= x
        while x>0:
            
            reverse_x = reverse_x * 10 + x % 10
            x //= 10 
        return reverse_x == org
              
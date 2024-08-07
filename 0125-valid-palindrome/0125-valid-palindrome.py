class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase_str = s.lower()
        alpanumeric_str = re.sub(r'[^a-z0-9]', '', lowercase_str)
        
        forward = alpanumeric_str
        backward = alpanumeric_str[::-1]
        
        if forward == backward:
            return True
        else:
            return False
        
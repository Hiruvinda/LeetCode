class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s =  s.rstrip()
        words = s.split(' ')
        last_word = words[-1]
        return len(last_word)
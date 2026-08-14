class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.aN(s[l]):
                l += 1
            while l < r and not self.aN(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True 
    def aN(self, x):
        return(ord('A') <= ord(x) <= ord('Z') or
        ord('a') <= ord(x) <= ord('z') or
        ord('0') <= ord(x) <= ord('9'))
         
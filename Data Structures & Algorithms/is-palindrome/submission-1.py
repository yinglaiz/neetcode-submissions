class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0 , len(s) - 1
        while l < r :
            while l<r and not self.Alphanum(s[l]) :     #for the pointer to not exceed the end of string
                l += 1
            while l<r and not self.Alphanum(s[r]) :
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l ,r = l+1 , r-1
        return True

    def Alphanum(self, s):
        return(ord('a') <= ord(s) <= ord('z') or
               ord('A') <= ord(s) <= ord('Z') or
               ord('0') <= ord(s) <= ord('9'))
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        def check(l,r):
            nonlocal res
            while l >= 0 and r <= len(s)-1 and s[l] == s[r] :
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1

            
        for i in range(len(s)):
            check(i,i)
            check(i,i+1)
        return res
        
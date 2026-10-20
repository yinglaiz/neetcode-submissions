class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def counter(l,r):
            nonlocal count
            ini = l
            while l >= 0 and r < len(s)  and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            
        for i in range(len(s)):
            counter(i,i)
            counter(i,i+1)
        return count
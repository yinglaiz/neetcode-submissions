class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freqcount  = {}
        l = 0
        maxfreq = 0 

        for r in range(len(s)):
            freqcount[s[r]] = 1 + freqcount.get(s[r],0) 
            maxfreq  =  max(maxfreq , freqcount[s[r]])

            while ((r - l + 1) - maxfreq) > k :
                freqcount[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
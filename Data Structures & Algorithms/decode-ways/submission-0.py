class Solution:
    def numDecodings(self, s: str) -> int:
        count = [0] * (len(s)+1)
        count[0] = 1

        for i in range(1, len(s)+1):
            if s[i-1] != '0':
                count[i] += count [i-1]
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                count[i] += count[i-2] 
        return count[len(s)]
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s)+1):
            for words in wordDict:
                istart = i - len(words)
                if istart >= 0 and dp[istart] and s[istart:i] == words:
                    dp[i] = True
                    break
        return dp[len(s)]
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def helper(i):
            if i <= 2:
                return i
            if i in memo:
                return memo[i]
            memo[i] = helper(i-1) +helper(i-2)
            
            return memo[i]
        return helper(n)
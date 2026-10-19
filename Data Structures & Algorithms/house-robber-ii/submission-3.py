class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self, houses):
        prev1, prev2 = 0,0
        for i in houses:
            cur = max(prev1 , prev2 + i)
            prev1, prev2 = cur, prev1
        return prev1
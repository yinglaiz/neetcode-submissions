class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmax, curmin = 1,1

        for n in nums:
            cands = (n , n*curmax,  n*curmin)
            curmax,curmin = max(cands), min(cands)
            res = max(res, curmax)
        return res
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr, maxi = 0,0
        l, r=0, len(heights)-1
        while l < r:
            curr = (r - l) * min(heights[l],heights[r])
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            maxi = max(maxi,curr)
        return maxi
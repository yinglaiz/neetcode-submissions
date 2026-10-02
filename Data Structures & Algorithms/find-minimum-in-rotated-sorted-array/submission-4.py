class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            midpos = start + (end - start) // 2
            if nums[midpos] > nums[end]:
                start = midpos + 1
            else:
                end = midpos
        return nums[start]
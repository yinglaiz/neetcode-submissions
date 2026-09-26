class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            midpos = start + (end - start) // 2
            if nums[midpos] == target:
                return midpos
            elif nums[midpos] < target:
                start = midpos + 1
            else:
                end = midpos - 1
        return -1

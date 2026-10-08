class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ints = set()
        for i in nums:
            if i in ints:
                return i 
            ints.add(i)

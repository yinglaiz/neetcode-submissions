class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        curr = numbers[l] + numbers[r]
        while curr != target:
            if curr > target:
                r -= 1
            if curr < target:
                l += 1
            curr = numbers[l] +numbers[r]
        return [l+1,r+1]

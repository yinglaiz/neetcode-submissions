class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        res = end
        while start <= end:
            k = start + (end - start) // 2
            time = 0
            for i in piles:
                time += (i + k - 1) // k
            if time > h:
                start = k + 1
            else:
                res = k
                end = k - 1
        return res

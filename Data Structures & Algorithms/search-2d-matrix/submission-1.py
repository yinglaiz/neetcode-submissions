class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        start = 0
        end = m*n - 1
        while start <= end:
            pos = start + (end - start)  // 2
            val = matrix[pos // n][pos % n]
            if val < target:
                start = pos + 1
            elif val > target:
                end = pos - 1
            else: 
                return True
        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix),len(matrix[0])
        start = 0
        end = m*n -1
        while start <= end:
            midpos = start + (end - start) // 2
            midval = matrix[midpos // n][midpos % n]
            if midval == target:
                return True
            elif midval < target:
                start = midpos + 1
            else:
                end = midpos - 1
        return False
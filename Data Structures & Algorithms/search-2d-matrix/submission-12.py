class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = (r + l) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][0] == target:
                return True
            else:
                l = mid + 1
        minrow = min(r,l)
        print(minrow)
        l = 0
        r = len(matrix[minrow]) - 1
        while l <= r:
            mid = (r + l) // 2
            if matrix[minrow][mid] > target:
                r = mid - 1
            elif matrix[minrow][mid] == target:
                return True
            else:
                l = mid + 1
        return False

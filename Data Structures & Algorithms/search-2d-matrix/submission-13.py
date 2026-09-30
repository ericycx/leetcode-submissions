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
        # minrow = min(l,r)
        minrow = r # its r because l <= r when either l == r and l + 1 or l == r and r - 1 
        if minrow < 0: #minrow could be -1 if target < matrix[0][0], so dont need to search -1 row
            return False
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

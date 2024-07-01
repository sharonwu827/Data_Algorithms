#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0 
        right = rows*cols
        while left < right:
            mid = left+(right-left)//2
            row = mid//cols
            col = mid%cols
            if matrix[row][col]==target:
                 return True
            if matrix[row][col]>target:
                right = mid
            else:
                left = mid+1
        return False
        

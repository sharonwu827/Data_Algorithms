#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        cache = {} 
        def dfs(row, col):
            # returns the minimum path sum starting from the current position (row, col) and ending at the bottom of the triangle.
            if (row, col) in cache:
                return cache[(row, col)]

            # At this point, we have reached the end of the path,
            # and the sum of the numbers in the current row is the final sum of the path starting from the top of the triangle.
            if row == n-1:
                return triangle[row][col]

            leftSum =  dfs(row+1, col)
            rightSum = dfs(row+1, col+1)

            minSum =  min(leftSum, rightSum) + triangle[row][col]
            cache[(row, col)] = minSum
            return minSum
        
        
        return dfs(0, 0)


            
# @lc code=end


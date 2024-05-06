#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        dp = [[float("inf")]*cols for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(rows):
            for j in range(cols):
                if i==0 and j>0:
                    dp[i][j] = dp[i][j-1]+grid[i][j]
                if j ==0 and i>0:
                    dp[i][j] = dp[i-1][j]+grid[i][j]
                if i>0 and j>0:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j])+grid[i][j]
        return dp[-1][-1]

                
            


# @lc code=end


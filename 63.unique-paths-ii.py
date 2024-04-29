#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid) 
        cols = len(obstacleGrid[0])

        dp= [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j]==1:
                    dp[i][j] = 0 
                else:
                    #需要特殊判断
                    if i>0 or j>0:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1] 
        return dp[rows-1][cols-1]
                

                
                
        


        
# @lc code=end


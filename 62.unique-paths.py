#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # dp[i][j]: # of possible unique paths from top left (0 ，0）to [i][j]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 or j ==0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        
        return dp[m-1][n-1]


        

        
# @lc code=end


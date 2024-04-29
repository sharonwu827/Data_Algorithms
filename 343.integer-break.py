#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        # dpi[i]: 分拆数字i，可以得到的最大乘积为dp[i]
        dp = [1]* n
        for i in range(2,n+1):
            for j in range(i):
                dp[i] = max(dp[i], dp[i-j]*j)
# @lc code=end



class Solution:
    def knapsack(self, n: int) -> int:
        dp = [ [0*(n] for _ in range(n)]
        dp[0][0]=0

        dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])
        

        
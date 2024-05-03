#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*n for _ in range(5)]
        # dp[0][i] no stock, no sell 
        # dp[1][i] one buy only 
        # dp[2][i] one buy and one sell
        # dp[3][i] one buy and one sell then one buy 
        # dp[4][i] one buy and one sell then one buy and one sell
        
        # 注意这个起始值dp[3][0] 
        dp[1][0] = dp[3][0] = - prices[0]

        maxProfit = 0 
        for i in range(1, n):
            dp[0][i] = dp[0][i-1]
            dp[1][i] = max(dp[0][i-1]-prices[i], dp[1][i-1])
            dp[2][i] = max(dp[1][i-1]+prices[i], dp[2][i-1])
            dp[3][i] = max(dp[2][i-1]-prices[i], dp[3][i-1])
            dp[4][i] = max(dp[3][i-1]+prices[i], dp[4][i-1])
            maxProfit = max(maxProfit, dp[4][i])
        return maxProfit
        
# @lc code=end


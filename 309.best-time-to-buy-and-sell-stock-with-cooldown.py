#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        dp = [ [0]*3 for _ in range(len(prices))]
        # dp[i][0]: not sell at ith day and dont have stock
        # dp[i][1]: sell at ith day and dont have stock
        # dp[i][2]: have stock

        dp[0][0] = 0 
        dp[0][1] = 0
        dp[0][2] = -prices[0]
        # dp[1][0] = max(dp[0][0], dp[0][1]) 
        # dp[1][1] = dp[0][2]+prices[1]
        # dp[1][2] = max(dp[0][2], dp[0][0]-prices[1])
              
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]) 
            dp[i][1] = dp[i-1][2]+prices[i] 
            dp[i][2] = max(dp[i-1][2], dp[i-1][0]-prices[i])
        return max(dp[-1])
       
        
# @lc code=end


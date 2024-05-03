#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0 
        # dp[i][0]: dont have stock at ith day and didnt sell
        # dp[i][1]: have stock at ith day
        # dp[i][2]: dont have stock at ith day and sell at ith day
        dp = [[0]*3 for _ in range(n)]
        dp[0][0] = 0 
        dp[0][1] = -prices[0]
        dp[0][2] = 0 
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][2], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])
            dp[i][2] = dp[i-1][1]+prices[i]
            maxProfit = max(dp[i][0], dp[i][1], dp[i][2])
        return maxProfit


       
        
# @lc code=end


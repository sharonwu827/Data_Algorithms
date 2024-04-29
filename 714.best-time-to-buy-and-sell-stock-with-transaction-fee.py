#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [ [0]* 2 for _ in range(len(prices))]
        #dp[0][0]: dont hold stock at ith day
        #dp[0][1]: hold stock at ith day
        dp[0][0] = 0 
        dp[0][1] = -prices[0]
        # dp[1][0] = max(dp[0][0], dp[0][1]+prices[1]-fee)
        # dp[1][1] = max(dp[0][1], dp[0][0]-prices[1])
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return max(dp[-1])
    

        
# @lc code=end


#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        1. dp[i]: max profit on ith day
        2. dp[0] = -prices[0]
           dp[1] = prices[1]-prices[0]
           dp[2] =  prices[2] - min(price[:2])
        3. dp[i] = max(dp[i-1],prices[i] -minprice)
        '''
        dp = [0] * len(prices)
        dp[0] = 0 
        min_price = prices[0] #注意这里不是 min_price = 0
        for i in range(1,len(prices)):
            min_price = min(min_price, prices[i])
            dp[i] = prices[i] - min_price
        return max(dp)
# @lc code=end


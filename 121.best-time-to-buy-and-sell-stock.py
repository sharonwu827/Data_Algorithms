#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i] the max profit at ith day
        n = len(prices)
        dp = [0]*n
        minPrice = float('inf')
        for i in range(n):
            minPrice = min(minPrice, prices[i])
            dp[i] = max(dp[i], prices[i] - minPrice)
        return max(dp)


# @lc code=end


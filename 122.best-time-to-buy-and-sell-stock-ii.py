#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0 
        for i in range(1, n):
            if prices[i]>prices[i-1]:
                maxProfit += prices[i]-prices[i-1]
        return maxProfit
            
               
            
        
# @lc code=end


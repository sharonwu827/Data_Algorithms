#
# @lc app=leetcode id=1475 lang=python3
#
# [1475] Final Prices With a Special Discount in a Shop
#

# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []
        res = prices.copy()
        for i, p in enumerate(prices):
            while stack and prices[stack[-1]]>p:
                ind = stack.pop()
                res[ind] = prices[ind]-p
            stack.append(i)
        return res
        
# @lc code=end


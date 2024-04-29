#
# @lc app=leetcode id=375 lang=python3
#
# [375] Guess Number Higher or Lower II
#

# @lc code=start
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # 如果猜数字大小k，而答案不是k的话，问题变为求解 (1, k-1) 和 (k+1, n) 的子问题需要的代价的最大值
        @cache
        def memorizationSearch(low, high):
            # 只剩一个数，该数一定是 所以所付代价=0
            if low == high: 
                return 0
            # 区间内没数了，不需要代价
            if low > high:
                return 0 
            res = float("inf")
            # need to ensure loop iterates over all numbers in the range [low, high]
            # inclusive of both low and high.
            for k in range(low, high+1):
                # we choose k and now can be split into (low+1, k-1) (k+1, high)
                left = memorizationSearch(low, k-1)
                right =  memorizationSearch(k+1, high)
                res = min(res, max(left, right)+k)
            return res
        return memorizationSearch(1, n)






        
        
# @lc code=end


#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][0] didnt stole at house i
        # dp[i][1]  stole at house i
        dp = [[0]*2 for _ in range(n)]
        dp[0][1] = nums[0]
        maxProfit = 0 
        if n==1:
            return nums[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0]+nums[i]
            maxProfit = max(maxProfit,dp[i][0], dp[i][1]  )
        return maxProfit

        
# @lc code=end


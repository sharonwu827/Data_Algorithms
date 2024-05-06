#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-float("inf")]*n
        dp[0] = max(nums[0], 1)
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1]*nums[i])
        return max(dp)
# @lc code=end


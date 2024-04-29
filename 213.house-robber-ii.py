#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            n = len(nums)
            dp = [0] * n 
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            return max(dp)
        
        if len(nums)<3:
            return max(nums)
        return max(helper(nums[1:]), helper(nums[:len(nums)-1]))
    
            
        
# @lc code=end


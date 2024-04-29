#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i][j]: the possible combinations for nums[:i] that sum up to target
        n = len(nums)
        dp = [ [0] * (target+1) for _ in range(n)]
        
        for i in range(target+1):
            if i%nums[0] == 0:
                dp[0][i] = 1
        
        for i in range(1, n):
            for j in range(1, target+1):
                if nums[i] <= j:
                    dp[i][j] += dp[i][j-nums[i]]
                else:
                    dp[i][j] += dp[i-1][j]
        return dp[n-1][target]
# @lc code=end


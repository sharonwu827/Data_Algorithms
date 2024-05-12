#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i][j]: the possible combinations for nums[:i] that sum up to j
        n = len(nums)
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(1, target+1):
                if nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] =  dp[i-1][j] + dp[i][j-nums[i-1]]
        return dp[-1][-1]





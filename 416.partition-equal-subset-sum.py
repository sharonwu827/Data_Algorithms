#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if sum(nums)%2!=0:
            return False
        target = sum(nums)//2
        dp = [[False]* (target+1)for _ in range(n+1)]
        # dp[i][j] return wheter from nums[:i-1] we can sum the element to j
        dp[0][0] = True
        for i in range(1, n+1):
            for j in range(target+1):
                if nums[i-1]<=j:
                    dp[i][j] = max(dp[i-1][j-nums[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][target]
    
        
        
        
                




    


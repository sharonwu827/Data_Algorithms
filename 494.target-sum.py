#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(n, curSum):
            if n == len(nums):
                if curSum == target:
                    return 1
                return 0 # 这里必须要返回0
            if (n, curSum) in cache:
                return cache[(n, curSum)]
            pos = dfs(n+1, curSum+nums[n]) # 这里不是pos = dfs(n+1, curSum+nums[n+1])
            neg = dfs(n+1, curSum-nums[n])
            cache[(n, curSum)] = pos+neg
            return pos+neg
        # the first integer in the array nums can be either positive or negative
        # and we need to consider both possibilities
        return dfs(0, 0)
     


        
# @lc code=end


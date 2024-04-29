#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        left = 0 
        right = 0 
        while right<len(nums):
            curSum+=nums[right]
            if curSum == k:
                res+=1
            while true:
                left+=1
        return res
        
# @lc code=end


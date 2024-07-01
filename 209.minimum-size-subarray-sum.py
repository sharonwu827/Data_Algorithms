#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        minLen = float('inf')
        left = 0
        curSum = 0
        for right in range(len(nums)):
            curSum+=nums[right]
            while curSum>=s:
                minLen = min(minLen, right-left+1)
                curSum-=nums[left]
                left+=1
        return minLen if minLen != float('inf') else 0
                
            
# @lc code=end


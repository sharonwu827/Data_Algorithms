#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largestSum  = float('inf')
        left = 0 
        curSum = 0
        for end in range(len(nums)):
            curSum += nums[end]
            if curSum > largestSum:
                largestSum = curSum
            
            

            

        


        
# @lc code=end


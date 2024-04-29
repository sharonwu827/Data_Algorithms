#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0 
        end = 0 
        maxSum = 0 
        for end in range(n):
            nums[start]+=nums[end]

            

        


        
# @lc code=end


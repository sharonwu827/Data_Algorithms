#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(i+1):
                res[i]+=nums[j]
        return res
            
        
# @lc code=end


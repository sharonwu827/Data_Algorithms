#
# @lc app=leetcode id=2369 lang=python3
#
# [2369] Check if There is a Valid Partition For The Array
#

# @lc code=start
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False]*len(nums)

        for i in range(2, n):
            if nums[i]==nums[i-1]==nums[i-2] or nums[i]==nums[i-1]:
                dp[i]=True
            if nums[i]-nums[i-1]==1 and nums[i-1]-nums[i-1]==1:
                dp[i]=True
            

            


        
        
            
          
                
        
# @lc code=end


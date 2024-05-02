#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0 
        for right in range(len(nums)):
            if right-left+1 >k:
                left+=1
            if right-left+1==k and nums[right]
            


        
# @lc code=end


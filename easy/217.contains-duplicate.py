#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_ = set(nums) # O(N)
        return len(set_)!=len(nums) #O(1)
        
# @lc code=end



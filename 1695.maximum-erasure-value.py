#
# @lc app=leetcode id=1695 lang=python3
#
# [1695] Maximum Erasure Value
#

# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        max_score = 0 
        left = 0 
        rigth = 0 
        dict_ = {}
        for right in range(len(nums)):
            dict_[nums[right]] = dict_.get(nums[right], 0)+1

            while right-left+1>len(dict_):
                dict_[nums[left]]-=1
                if not  dict_[nums[left]]:
                    del dict_[nums[left]]
                left+=1
            if right-left+1==len(dict_):
                max_score = max(max_score, sum(nums[left:right+1]))
        return max_score
            
            
        
# @lc code=end


#
# @lc app=leetcode id=2302 lang=python3
#
# [2302] Count Subarrays With Score Less Than K
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0 
        left = 0 
        for right in range(len(nums)):
            while (right-left+1) * sum(nums[left:right+1])>=k:
                left+=1
            res+= right-left+1
        return res


        
# @lc code=end


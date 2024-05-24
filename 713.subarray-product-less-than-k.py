#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0 
        right = 0 
        res = 0 
        curProduct = 1
        if k <=1:
            return 0
        for right in range(len(nums)):
            curProduct *= nums[right]
            while curProduct >= k:
                curProduct = curProduct//nums[left]
                left += 1
            res+= right-left+1
        return res
                
                
        
# @lc code=end


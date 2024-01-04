#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # return number of combination 
        
        start = 0 
        res = 0
        cur_product = 1

        for end in range(start, len(nums)):
            cur_product *= nums[end]
            while cur_product>=k and start<=end:
                cur_product /= nums[start]
                start += 1
            res+= end-start+1 # add the combination within the window
        return res
     
# @lc code=end


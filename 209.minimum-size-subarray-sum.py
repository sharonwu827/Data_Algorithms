#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        cur = 0
        min_len = float("inf")

        for right in range(left, len(nums)):
            cur+=nums[right]
            while cur >= target:
                # mean we find a target, we update the res
                min_len = min(min_len, right-left+1)
                cur -=nums[left]
                left+=1
        
        return min_len if min_len != float("inf") else 0
                
       
        
        
# @lc code=end


#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        start = 0 
        cur_sum = 0

        for end in range(len(nums)):
            cur_sum += nums[end]

            # Check if the condition is met to shorten the subarray length
            if cur_sum >= target:
                min_len = min(min_len, end - start + 1)
                
                # Shorten the subarray by moving the start pointer
                cur_sum -= nums[start]
                start += 1
                
        return 0 if min_len == float("inf") else min_len
      
        
# @lc code=end


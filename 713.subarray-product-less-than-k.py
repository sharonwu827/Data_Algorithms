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
        curProduct = 1
        cnt = 0
  
        for right in range(len(nums)):
            curProduct *= nums[right]
            while left<=right and curProduct>=k:
                curProduct = curProduct//nums[left]
                left+=1
            # cannot be cnt+=1
            # This would simply count the number of times the right pointer moves. 
            # It doesn't consider the size of the subarray between left and right. 
            # It would just count each time the right pointer moves forward, regardless of the size of the subarray.
            cnt+=right - left + 1
        return cnt
                
        
# @lc code=end


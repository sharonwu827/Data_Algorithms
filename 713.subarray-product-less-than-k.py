#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
           return 0
        left = 0 
        curProduct = 1
        res = 0
  
        for right in range(len(nums)):
            curProduct *= nums[right]
            #注意left <= right这个条件
            while curProduct>=k:
                curProduct = curProduct//nums[left]
                left+=1
            # cannot be cnt+=1
            # This would simply count the number of times the right pointer moves. 
            # It doesn't consider the size of the subarray between left and right. 
            # It would just count each time the right pointer moves forward, regardless of the size of the subarray.
            res+=right - left + 1
        return res
                
                
        
# @lc code=end


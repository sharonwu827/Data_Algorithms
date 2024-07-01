#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#

# @lc code=start
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        maxWidth = 0
        for i, num in enumerate(nums):
            while not stack or nums[stack[-1]]>num:
                stack.append(i)
            if stack and nums[stack[-1]]<=num:
                maxWidth = max(maxWidth, i-stack[-1])
        return maxWidth
        
# @lc code=end


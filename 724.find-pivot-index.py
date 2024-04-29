#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * (n+1)
        right = [0] * (n+1)
        for i in range(n):
            left[i+1] = nums[i]+left[i]
        for j in range(n-1, -1, -1):
            right[j+1] = nums[j]+right[j]
        
        for k in range(n+1):
            if left[k]==right[k]:
                return k-1



        
# @lc code=end


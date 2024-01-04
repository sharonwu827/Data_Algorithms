#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #return index
        left = 0 
        right = len(nums)-1
        while left<right:
            mid = left+(right-left)//2
            if nums[mid]>nums[mid+1]:
                # num[mid] 可能为峰值，而 nums[mid+1] 必然不为峰值
                # 于是让 r=mid 从左半部分继续找峰值
                right = mid
            else:
                left = mid+1
        return left

      
# @lc code=end


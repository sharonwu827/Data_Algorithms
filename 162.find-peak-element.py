#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums)-1
        while left<right:
            mid = left+(right-left)//2
            if nums[mid]>nums[mid+1]:
                right = mid
            else:
                left = mid+1
        return left


        
           

                        
# @lc code=end


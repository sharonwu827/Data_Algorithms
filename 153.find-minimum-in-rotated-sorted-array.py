#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums)-1
        while left<right:
            mid = left+(right-left)//2
            # from left to right, increasing
            if nums[mid]<nums[right]:
                right = mid
            else:
                left = mid+1
        return nums[left]


        
        
# @lc code=end


#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)-1
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                return mid
            if nums[mid]>nums[right]:
                if target<nums[mid]:
                    right = mid-1
                else:
                    right =left+1
            else:
                if target>nums[mid]:
                    left = mid+1
                else:
                    right=mid-1
        return -1
                



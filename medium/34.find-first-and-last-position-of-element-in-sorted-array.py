#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findLeft(nums, target):
            left = 0 
            right = len(nums)-1
            while left<right:
                mid = left+(right-left)//2
                # find the min index that >= target
                if nums[mid]>=target:
                    right = mid
                else:
                    left = mid+1
            return left
        
        left = findLeft(nums, target)
        if not nums or nums[left]!=target:
            return [-1, -1]
        
        def findRight(nums, target):
            left = 0 
            right = len(nums) #这里不是len（nums)
            while left<right:
                mid = left+(right-left)//2
                # find the minimum mid that > target
                if nums[mid]>target:
                    right = mid
                else:
                    left = mid+1
            return left-1
        
        right = findRight(nums, target)

        return [left, right]
        

               
# @lc code=end


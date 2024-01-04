#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)-1
        while left<right:
            mid = left+(left+right)//2
            cnt = 0 
            for i in mid:
                if nums[i]<nums[mid]:
                    cnt+=1
                
        
# @lc code=end


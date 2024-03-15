#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0 
        right = len(nums)-1
        while left < right:
            while left < right and nums[right]%2!=0:
                right-=1
            while left<right and nums[left]%2==0:
                left+=1
            nums[left], nums[right] = nums[right], nums[left]
        return nums

# @lc code=end


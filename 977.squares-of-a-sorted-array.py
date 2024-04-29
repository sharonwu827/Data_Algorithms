#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        left = 0 
        right = len(nums)-1
        while left<=right:
            if nums[left]**2<=nums[right]**2:
                res.append(nums[right]**2)
                right-=1
            else:
                res.append(nums[left]**2)
                left+=1
        return res[::-1]
                
# @lc code=end


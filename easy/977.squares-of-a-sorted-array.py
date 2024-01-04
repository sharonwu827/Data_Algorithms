#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l = 0 
        r = len(nums)-1
        while l <= r:
            if nums[l]**2 < nums[r]**2:
                res.append(nums[r]**2)
                r-=1
            else:
                res.append(nums[l]**2)
                l+=1
        return res[::-1]

        
# @lc code=end


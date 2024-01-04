#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0 
        r = len(nums) - 1
        while l < r:
            if nums[l]+nums[r] > target:
                r-=1
            elif nums[l]+nums[r] < target:
                l+=1
            else:
                return [l, r]
            
        # O(logN), O(1)
# @lc code=end


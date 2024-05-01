#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i, num in enumerate(nums):
            if i > k:
                window.remove(nums[i - k -1])
            if num in window:
                return True
            window.add(num)
        return False



        
# @lc code=end


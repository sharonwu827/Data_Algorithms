#
# @lc app=leetcode id=2962 lang=python3
#
# [2962] Count Subarrays Where Max Element Appears at Least K Times
#

# @lc code=start
from collections import Counter


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        def isValid(arr):
            if not arr:
                return False
            max_num = max(arr)
            frequency = Counter(arr)[max_num]
            return frequency >= k

        numSubarr = 0 
        left = 0 
        right = 0 
        for right in range(len(nums)):
            while not isValid(nums[left:right+1]):
                left += 1
            numSubarr += right - left + 1

        return numSubarr



        
# @lc code=end


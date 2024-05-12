#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def getLongestConsecutive(i):
            if i == len(nums):
                return 
            for i in range(len(nums)):
                res = getLongestConsecutive(nums[i-1])
        return 1



        
# @lc code=end


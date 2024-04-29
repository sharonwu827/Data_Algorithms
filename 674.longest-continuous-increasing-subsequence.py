#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        left = 0 
        right = 0 
        max_len = 1
        for right in range(1, len(nums)):
            # cannot use while
            # if using while,this loop will keep executing 
            # this loop is problematic because it doesn't change the value of right
            while nums[right]<=nums[right-1]:
                left=right
            max_len = max(max_len, right-left+1)
        return max_len
            
                

        



 
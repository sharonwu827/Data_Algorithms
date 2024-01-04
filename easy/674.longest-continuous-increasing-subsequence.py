#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # 窗口不固定
        start = 0 
        cur_len = 1
        max_len = 1
        for end in range(start+1, len(nums)):

            # 此时窗口不合法
            # use if here as we are interested in checking the condition for each element 
            # and then performing actions based on that condition.
            # We don't need a while loop 
            # because we are handling each element one by one. 
            # If the condition is true, we continue the current increasing subsequence; 
            # otherwise, we update the maximum length and start a new increasing subsequence.
            if nums[end]<=nums[end-1]:
                start+=1
                cur_len = 1
            else:
                cur_len+=1
                max_len = max(cur_len, max_len)
        return max_len

             
# @lc code=end


#
# @lc app=leetcode id=1695 lang=python3
#
# [1695] Maximum Erasure Value
#

# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # return max sum of subarray which doesn't include duplicate
        # 窗口不固定
        max_sum = 0
        cur_sum = 0
        start = 0
        dict_ = {}
        for end in range(len(nums)):
            dict_[nums[end]] = dict_.get(nums[end],0)+1
            while len(dict_) < end-start+1: # there is duplicate in the window
                dict_[nums[start]]-=1
                if not dict_[nums[start]]:
                    del dict_[nums[start]]
                cur_sum-=nums[start]
                start+=1
            
            cur_sum+= nums[end]
            max_sum = max(cur_sum, max_sum)
        return max_sum
              
# @lc code=end


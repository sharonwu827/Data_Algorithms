#
# @lc app=leetcode id=2958 lang=python3
#
# [2958] Length of Longest Subarray With at Most K Frequency
#

# @lc code=start
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dict_ = defaultdict(int)
        left = 0 
        maxLen = -float('inf')
        for right in range(len(nums)):
            dict_[nums[right]] += 1
            # while max(dict_.values()) > k:
            while dict_[nums[right]] > k:
                dict_[nums[left]] -= 1
                if dict_[nums[left]] == 0:
                    del dict_[nums[left]]
                left+=1
        
            maxLen = max(maxLen, right - left + 1)
        return maxLen

        
# @lc code=end


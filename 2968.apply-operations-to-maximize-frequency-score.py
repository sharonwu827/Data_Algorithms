#
# @lc app=leetcode id=2968 lang=python3
#
# [2968] Apply Operations to Maximize Frequency Score
#

# @lc code=start
from typing import List

from typing import List

from typing import List

class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array first
        n = len(nums)
        max_score = 0
        window_sum = 0
        left = 0
        
        for right in range(n):
            window_sum += nums[right]
            while (right - left + 1) * nums[right] - window_sum > k:
                window_sum -= nums[left]
                left += 1
            max_score = max(max_score, right - left + 1)
        
        return max_score






        
# @lc code=end


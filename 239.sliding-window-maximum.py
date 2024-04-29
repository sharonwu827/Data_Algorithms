#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        result = []
        #  stores indices of elements that currently within the sliding window.
        window = deque()
        for right in range(len(nums)):
            while window and right-window[0]+1>k:
                window.popleft()
            while window and nums[window[-1]]<nums[right]:
                window.pop()
            window




        
# @lc code=end


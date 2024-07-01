#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#

# @lc code=start
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        preSum = [0] * (len(nums) + 1)
        for i in range(1, len(preSum)):
            preSum[i] = preSum[i-1] + nums[i-1]

        queue = deque()
        res = float('inf')
        for i, val in enumerate(preSum):
            while queue and val-preSum[queue[0]]>=k:
                




                



# @lc code=end


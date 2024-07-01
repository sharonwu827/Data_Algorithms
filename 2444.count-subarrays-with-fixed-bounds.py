#
# @lc app=leetcode id=2444 lang=python3
#
# [2444] Count Subarrays With Fixed Bounds
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], min_k: int, max_k: int) -> int:
        left = 0 
        # minK 上一次出现的位置 
        minInd = -1
        # maxK 上一次出现的位置
        maxInd = -1
        res = 0
        for i, val in enumerate(nums):
            if val == min_k:
                minInd = i
            if val == max_k:
                maxInd = i
            if val < min_k or val > max_k:
                left = i + 1
            res += max(0, min(minInd, maxInd) - left + 1)
        return res
                
            


        
# @lc code=end


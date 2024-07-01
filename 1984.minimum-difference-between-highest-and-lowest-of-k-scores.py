#
# @lc app=leetcode id=1984 lang=python3
#
# [1984] Minimum Difference Between Highest and Lowest of K Scores
#

# @lc code=start
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # minDiff = float('inf')
        # def backtrack(startInd, path):
        #     nonlocal minDiff
        #     if len(path) == k:
        #         curDiff = max(path) - min(path)
        #         minDiff = min(minDiff, curDiff)
        #         return
        #     if len(path) > k:
        #         return
        #     for i in range(startInd, len(nums)):
        #         path.append(nums[i])
        #         backtrack(i + 1, path)
        #         path.pop()
        #     return minDiff
        # backtrack(0, [])
        # return minDiff
        nums.sort()
        
        
# @lc code=end


#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() 
        def backtrack(startInd, path):
            res.append(path.copy())
            for i in range(startInd, len(nums)):
                if i>startInd and nums[i] == nums[i-1]:
                    continue # skip the current iteration and move to the next iteration of the loop immediately.
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        backtrack(0, [])
        return res
# @lc code=end


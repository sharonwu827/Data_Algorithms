#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(startInd, path):
            if sum(path)==target:
                res.append(path.copy())
                return 
            if sum(path)>target:
                return
            for i in range(startInd, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path)
                path.pop()
        backtrack(0, [])
        return res




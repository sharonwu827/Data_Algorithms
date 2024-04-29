#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        candidates.sort()
        def backtrack(startInd, path):
            if sum(path) == target:
                res.append(path.copy())
                return 
            if sum(path)>target:
                return 
            for i in range(startInd, len(candidates)):
                if i>startInd and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1, path)
                path.pop()
        backtrack(0, [])
        return res
       
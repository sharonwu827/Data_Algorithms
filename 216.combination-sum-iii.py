#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(startInd, path):
            if sum(path) == n and len(path) == k:
                res.append(path.copy())
                return 
            
            if sum(path)> n or len(path)>k:
                return

            for i in range(startInd, 10):
                path.append(i)
                backtrack(i+1, path)
                path.pop()

        backtrack(1, [])
        return res
      
        
# @lc code=end


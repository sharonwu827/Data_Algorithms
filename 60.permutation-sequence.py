#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        used = [0] * (n+1)
        def backtrack(path):
            nonlocal res, k
            if len(path) == n:
                k -= 1
                if k == 0:
                    res = path.copy()
                return 
            for i in range(1, n+1):
                if used[i] == 1:
                    continue
                used[i] = 1
                path.append(str(i))
                backtrack(path)
                #if res: check is necessary to stop the backtracking process
                if res:
                    return
                path.pop()
                used[i] = 0
        backtrack([])
        return ''.join(res)   
# @lc code=end


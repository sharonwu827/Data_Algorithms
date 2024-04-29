#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtracking(startInd, path):
            # not necessary because the loop for i in range(start, n + 1): already ensures that i goes up to n.
            # if startInd == n:
            #     return 
            if len(path) == k:
                res.append(path.copy())
                # we need return here
                # 1. Termination Condition: It ensures that the backtracking recursion terminates 
                # when the length of the current combination curr reaches k
                # if we don't return after appending, the function would continue exploring other combinations even though we have already found one of the desired length
                return 
            for i in range(startInd, n+1):
                path.append(i)
                backtracking(i+1, path) # not startInd+1
                path.pop()

        backtracking(1, [])
        return res
# @lc code=end


#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#

# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def dfs(left, right, apoints, bpoints):
            if left == right:
                return 
            dfs(left+1, right)
            dfs(left, right-1)

        
# @lc code=end


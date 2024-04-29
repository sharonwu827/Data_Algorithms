#
# @lc app=leetcode id=959 lang=python3
#
# [959] Regions Cut By Slashes
#

# @lc code=start
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows = len(grid)
        columns = len(grid[0])
        new_grid = [[0]* (3*columns) for _ in range(rows*3)]
        def dfs(x, y):
            if  not (0 <= x < 3 * rows and 0 <= y < 3 * columns):
                return 
            if new_grid[x][y] != 0:
                return 
            
        
# @lc code=end


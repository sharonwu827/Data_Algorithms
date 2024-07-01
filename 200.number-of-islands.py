#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])
        res = 0 
        def dfs(x, y):
            if not (0 <= x < rows and 0 <= y < cols):
                return
            if grid[x][y]!='1':
                return 
            for i, j in dirs:
                grid[x][y] = '2'
                new_x = x + i
                new_y = y + j
                dfs(new_x, new_y)
            return 1
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    res+=dfs(i, j)
        return res
        
      
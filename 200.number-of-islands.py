#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [(0,1),(1,0),(-1,0), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        def dfs(x, y):
            if not (0<=x<rows and 0<=y<cols):
                return 
            if grid[x][y]!='1':
                return 
            grid[x][y]='999'
            for i, j in dir:
                new_x = x+i
                new_y = y+j
                if (0<=new_x<rows and 0<=new_y<cols):
                    dfs(new_x, new_y)
            return 1
        
        res = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y]=='1':
                    res+=dfs(x, y)
        return res


       
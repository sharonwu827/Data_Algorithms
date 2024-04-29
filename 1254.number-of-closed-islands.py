#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#

# @lc code=start
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows = len(grid)
        columns = len(grid[0])
        def traverse(x, y):
            if not (0<=x<rows and 0<=y<columns):
                return 
            if grid[x][y]!=0:
                return
            for i, j in dir:
                new_x = x+i
                new_y = y+j
                traverse(new_x, new_y)
            return 1
            
            

        for i in range(rows):
            traverse(i, 0)
            traverse(i, columns-1)
        for j in range(columns):
            traverse(0, j)
            traverse(rows-1, j)

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 2:
                    grid




                
                 
# @lc code=end


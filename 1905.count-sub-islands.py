#
# @lc app=leetcode id=1905 lang=python3
#
# [1905] Count Sub Islands
#

# @lc code=start
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows = len(grid1)
        columns = len(grid1[0])

        # traverse grid 2
        # if we find an island, we need to find the value in grid1 
        # 如果岛屿 B 中存在一片陆地，在岛屿 A 的对应位置是海水，那么岛屿 B 就不是岛屿 A 的子岛。
        def traverse(grid, x, y):
            if not (0<=x<rows and 0<=y<columns):
                return 
            if grid[x][y]!=1:
                return 
            grid[x][y]=0
            for i, j in dir:
                new_x = x+i
                new_y = y+j
                traverse(grid, new_x, new_y)
        
        for i in range(rows):
            for j in range(columns):
                if grid1[i][j] ==0 and grid2[i][j]==1:
                    traverse(grid2, i, j)
        
                
        res = 0
        for i in range(rows):
            for j in range(columns):
                if grid2[i][j]==1:
                    res+=1
                    # mark the adj land to be 0
                    traverse(grid2, i, j)
        return res
# @lc code=end


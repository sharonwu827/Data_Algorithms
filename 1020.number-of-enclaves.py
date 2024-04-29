#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#

# @lc code=start
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows = len(grid)
        columns = len(grid[0])
        # visited = set()
        def dfs(x ,y):
            if not (0<=x<rows and 0<=y<columns):
                return 0
            if grid[x][y]!=1:
                return 0
            # if (x, y) in visited:
            #     return 0
            # visited.add( (x, y))
            grid[x][y] = 2
            for i, j in dir:
                new_x = x+i
                new_y = y+j
                dfs(new_x, new_y)
        
        for i in range(rows):
            dfs(i, 0)
            dfs(i, columns-1)
        for j in range(columns):
            dfs(0, j)
            dfs(rows-1, j)

        res = 0 
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]==1:
                    res+=1
        return res


# @lc code=end

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        def dfs(x ,y):
            if not (0<=x<rows and 0<=y<columns):
                return 
            if grid[x][y]!=1:
                return 
            if (x, y) in visited:
                return 
            visited.add((x,y))
            for i, j in dir:
                new_x = x+i
                new_y = y+j
                dfs(new_x, new_y)
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]==1:
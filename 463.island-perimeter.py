#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        res = 0 
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] ==1:
                    res+=4
                    for i, j in dir:
                        new_x = i+x
                        new_y = j+y
                        if 0<= new_x <rows and 0<=new_y<cols and grid[new_x][new_y] == 1:
                            res-=1
        return res    
        
# @lc code=end


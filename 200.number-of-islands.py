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
        queue = deque()
        res = 0 

        for x in range(rows):
            for y in range(cols):
                if grid[x][y]=='1':
                    grid[x][y]='2'
                    res +=1
                    queue.append((x,y))
                    while queue:
                        x, y = queue.popleft()
                        for i, j in dir:
                            new_x = x+i
                            new_y = y+j
                            if 0<=new_x<rows and 0<=new_y<cols:
                                if grid[new_x][new_y]=='1':
                                    queue.append((new_x,new_y))
                                    grid[new_x][new_y]='2'
        return res
                        



            

       
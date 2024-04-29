#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows = len(grid)
        columns = len(grid[0])
        maxArea = 0 
        curArea = 0
        queue = deque()

        def bfs(x, y):
            queue.append((x,y))
            grid[x][y]=2
            curArea = 1
            while queue:
                x, y = queue.popleft()
                for i, j in dir:
                    new_x = x+i
                    new_y = y+j
                    if 0<=new_x<rows and 0<=new_y<columns:
                        if grid[new_x][new_y]==1:
                            curArea+=1
                            queue.append((new_x, new_y))
            return curArea

                    
        
        for x in range(rows):
            for y in range(columns):
                if grid[x][y]==1:
                  curArea =bfs(x, y)
                  maxArea = max(maxArea, curArea)
        
        return maxArea
                




#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dir = [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0]==1 or grid[-1][-1] == 1:
            return -1
        queue = deque()
        queue.append((0, 0, 1))  # x, y, lenght of path

        while queue:
            x, y, path = queue.popleft()
            grid[x][y] =2
            if x == rows-1 and y == cols-1:
                return path 
            for i, j in dir:
                newX = x+i
                newY = y+j
                if (0<=newX<rows and 0<=newY<cols) and grid[newX][newY] == 0:
                    queue.append((newX, newY, path+1))
                    grid[newX][newY] =2
            
        return -1

                

        
        
        
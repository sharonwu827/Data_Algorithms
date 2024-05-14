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
        queue.append((0, 0))
        path = 1
        grid[0][0] = 2
        while queue:
            # 对BFS的某一层的中所有点向8个方向进行扩展
            # 每一轮搜索结束后，我们将搜索轮数增加 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                # 如果扩展的点到达了终点 直接返回
                if x == rows-1 and y==cols-1:
                    return path
                for i, j in dir:
                    newX = x+i
                    newY = y+j
                    if (0<=newX<rows and 0<=newY<cols) and grid[newX][newY]==0:
                        queue.append((newX, newY))
                        grid[newX][newY] = 2
            # 对某一层的元素都求判定过后，距离加1(同一个层次中的所有点的距离距离起点都是相等的）
            path+=1  
        return -1

                
# @lc code=end


#
# @lc app=leetcode id=1162 lang=python3
#
# [1162] As Far from Land as Possible
#

# @lc code=start
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        dir = [(0,1),(1,0),(-1,0), (0, -1)]
        rows = len(grid)
        columns = len(grid[0])
        queue = deque()
        
        # 找到所有的水单元格并将其加入队列
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0:
                    queue.append((i,j,0))
        
        # 如果整个网格都是陆地或都是水，返回 -1
        if len(queue) == 0 or len(queue) == rows * columns:
            return -1
        
        max_shortest_distance = -1
        while queue:
            x, y, step = queue.popleft()
            
            for i, j in dir:
                new_x = x+i
                new_y = y+j
                if (0<=new_x<rows and 0<=new_y<columns):
                    if grid[new_x][new_y] == 1:
                        max_shortest_distance = max(max_shortest_distance, step+1)
                    elif grid[new_x][new_y] == 0:
                        queue.append((new_x, new_y, step+1))
                        grid[new_x][new_y] = -1  # 将访问过的水单元格标记为 -1，避免重复访问
        
        return max_shortest_distance if max_shortest_distance != -1 else -1

        


        
# @lc code=end


#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc code=start
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        # # 保存岛屿编号及对应面积
        # island ID: island area
        area_mapping = {}  
        starting_island_index = 2
        def getArea(x, y, island_id):
            if not (0 <= x < rows and 0 <= y < columns):
                return 0
            if grid[x][y] != 1:
                return 0
            if (x, y) in visited:
                return 0
            visited.add((x, y))
            size = 1
            for i, j in dir:
                new_x = x+i
                new_y = y+j
                cur_area+= getArea(x, y, island_id)
            return size
        
        for i in range(rows):
            for j in range(columns):
                # 遍历整个矩阵的过程中，对不同的岛屿进行编号 当遍历到新的岛屿时，岛屿编号加1
                if grid[i][j]==1:
                    size = getArea(i, j, starting_island_index)
                    area_mapping[starting_island_index] = size
                    grid[i][j] = size
                    starting_island_index+=1 
        # for each 0 get the total size of neihgbor Islands
        for i in range(n):
            for j in range(n):
                sum = 0
                # 如果该位置等于0， 并且变为1后能连接不同的岛屿，则将所求得的面积取大小
                set = []  # 去重数组
                if grid[i][j] == 0:
                    sum = 1
                    # 求和，去重
                    if i - 1 >= 0 and grid[i - 1][j] != 0:
                        if grid[i - 1][j] not in set:
                            set.append(grid[i - 1][j])
                            sum += areaMap[grid[i - 1][j]]
                    if i + 1 < n and grid[i + 1][j] != 0:
                        if grid[i + 1][j] not in set:
                            set.append(grid[i + 1][j])
                            sum += areaMap[grid[i + 1][j]]
                    if j - 1 >= 0 and grid[i][j - 1] != 0:
                        if grid[i][j - 1] not in set:
                            set.append(grid[i][j - 1])
                            sum += areaMap[grid[i][j - 1]]
                    if j + 1 < n and grid[i][j + 1] != 0:
                        if grid[i][j + 1] not in set:
                            set.append(grid[i][j + 1])
                            sum += areaMap[grid[i][j + 1]]
                max_area = max(max_area, sum)
        if max_area == 0:
            # 还有一种情况，如果矩阵全是1，则max_area结果为0，所以直接返回矩阵的大小
            return len(grid)**2

                
                


 
                  


        
# @lc code=end


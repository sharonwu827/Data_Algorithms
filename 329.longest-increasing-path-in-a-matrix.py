#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dir = [(1, 0), (0, 1), (-1, 0),(0, -1)]
        rows = len(matrix)
        cols = len(matrix[0])
        cache = [[1]*cols for _ in range(rows)] 
        def dfs(x, y):
            if not (0<=x<rows and 0<=y<cols):
                return 
            if cache[x][y] != 1:
                return cache[x][y] 
            for i, j in dir:
                new_x = x+i
                new_y = y+j
                if (0<=new_x<rows and 0<=new_y<cols) and matrix[x][y]<matrix[new_x][new_y]:
                    #这么写是错的
                    # cache[x][y] = max(dfs(new_x, new_y), cache[x][y])+1
                    cache[x][y] = max(dfs(new_x, new_y)+1, cache[x][y])
            return cache[x][y]
        
        maxLen = 1
        for x in range(rows):
            for y in range(cols):
                maxLen = max(maxLen, dfs(x, y))
        return maxLen

        
                    

   
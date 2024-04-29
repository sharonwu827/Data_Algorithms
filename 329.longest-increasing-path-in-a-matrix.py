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
        columns = len(matrix[0])
        # visited = set()
        dp = [[0] * columns for _ in range(rows)]
        
        def getLen(x, y):
            if not (0<=x<rows and 0<=y<columns):
                return 0
            if dp[x][y]!=0:
                return dp[x][y]
            for i, j in dir:
                new_x = x+i
                new_y = y+j
                if (0<=new_x<rows and 0<=new_y<columns) and matrix[new_x][new_y]>matrix[x][y]:
                     dp[x][y] = max(dp[x][y], getLen(new_x, new_y) + 1)
            # dp[x][y] +=1 # It adds 1 to the length because we are including the current cell in the path.
            # returns the length of the longest increasing path starting from the current cell (x, y)
            # This value is needed for the recursive calls to getLen to determine the length of the path from neighboring cells.
            return dp[x][y]
        
        max_len = 0
        for i in range(rows):
            for j in range(columns):
                cur_len = getLen(i, j)
                max_len = max(max_len, cur_len)
        return max_len

   
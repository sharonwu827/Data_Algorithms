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
        cache = defaultdict() # store the longest path at position(x,y)
        def memorization(x, y):
            if not (0<=x<rows and 0<=y<cols):
                return 
            if (x, y) in cache:
                return cache[(x, y)]
            curLen = 1
            for i, j in dir:
                newX = x+i
                newY = y+j
                if (0<=newX<rows and 0<=newY<cols) and matrix[x][y]<matrix[newX][newY]:
                    curLen = max(curLen,  memorization(newX, newY)+1)
            cache[(x,y)] = curLen
            return curLen
        
        longestLen = 0
        for x in range(rows):
            for y in range(cols):
                longestLen = max(longestLen, memorization(x, y))
        return longestLen

            

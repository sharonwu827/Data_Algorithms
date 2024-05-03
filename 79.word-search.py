#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        rows = len(board)
        cols = len(board[0])
        visited = set() 
        def dfs(x, y, ind):
            '''
            check board[x][y] == word[ind]
            '''
            if ind == len(word):
                return True
            if not (0<=x<rows and 0<=y<cols):
                return False
            # means we have checked the end of word
            if (x,y) in visited:
                return False
            if board[x][y] != word[ind]:
                return False
            visited.add((x, y))
            for i, j in dir:
                new_x =x+i
                new_y = y+j
                #注意这个写法
                if dfs(new_x, new_y, ind+1):
                    return True
            visited.remove((x, y))

        for x in range(rows):
            for y in range(cols):
                if dfs(x, y, 0):
                    return True
        return False


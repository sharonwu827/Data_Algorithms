#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
       
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows = len(image)
        columns = len(image[0])
        colorToChange = image[sr][sc]
        def dfs(x, y):
            if not (0<=x<rows and 0<=y<columns):
                return
            if image[x][y] != colorToChange:
                return
            # 这个条件不能少
            # necessary to prevent infinite recursion 
            if image[x][y]==color:
                return 
            image[x][y] = color
            for i, j in dir:
                new_x = x+i
                new_y = y+j
                dfs(new_x, new_y)
        dfs(sr, sc)
        return image

            

# @lc code=end


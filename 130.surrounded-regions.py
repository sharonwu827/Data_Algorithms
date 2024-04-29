#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows = len(board)
        columns = len(board[0])
        
        # mark the border and its nearby 'O's a different mark ('B')
        def dfs(x, y):
            if not (0 <= x < rows and 0 <= y < columns):
                return
            if board[x][y] != 'O':
                return
            board[x][y] = 'B'
            for i, j in dir:
                new_x = x + i
                new_y = y + j
                if 0 <= new_x < rows and 0 <= new_y < columns:
                    if board[new_x][new_y] == 'O':
                        dfs(new_x, new_y)

        # Traverse the border and mark connected 'O's as 'B'
        for i in range(columns):
            dfs(0, i)
            dfs(rows - 1, i)
        for j in range(rows):
            dfs(j, 0)
            dfs(j, columns - 1)

        # Flip 'O's to 'X's and restore 'B's to 'O's
        for x in range(rows):
            for y in range(columns):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == 'B':
                    board[x][y] = 'O'

        

        
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms or not rooms[0]:
            return
        dir = [(0,1),(1,0),(-1,0), (0, -1)]
        rows = len(rooms)
        columns = len(rooms[0])
        queue = deque()

        def bfs(x, y):
            queue.append((x,y))
            while queue:
                x, y = queue.popleft()
                for i, j in dir:
                    new_x = x+i
                    new_y = y+j
                    if (0<=new_x<rows and 0<=new_y<columns):
                        # for the empty room, fill the shortest step
                        if rooms[new_x][new_y]== 2**31 - 1:
                            rooms[new_x][new_y]= min(rooms[x][y]+1, rooms[new_x][new_y])
                            queue.append((new_x, new_y))
        
        for x in range(rows):
            for y in range(columns):
                if rooms[x][y] == 0:
                     queue.append((x,y))
                     
                
                        




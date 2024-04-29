#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dir = [(0,1),(1,0),(-1,0), (0, -1)]
        rows = len(grid)
        columns = len(grid[0])
        queue = deque()
        fresh_orange = 0 
        time_needed = 0 
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] ==1:
                    fresh_orange+=1
                if grid[i][j] ==2:
                    queue.append((i,j, time_needed))
        while queue:
            for _ in range(len(queue)):
                x, y, time_needed = queue.popleft()
                for i, j in dir:
                    new_x = x+i
                    new_y = y+j
                    if (0<=new_x<rows and 0<=new_y<columns) and grid[new_x][new_y]==1:
                        grid[new_x][new_y]=2
                        fresh_orange -=1
                        queue.append((new_x, new_y, time_needed+1))

        return -1 if fresh_orange else time_needed
                
           
           
# # @lc code=end
# class Solution:
#     def wallsAndGates(self, rooms: List[List[int]]) -> None:
#         """
#         Do not return anything, modify rooms in-place instead.
#         """
#         dir = [(0,1),(1,0),(-1,0), (0, -1)]
#         rows = len(rooms)
#         columns = len(rooms[0])
#         queue = deque()

#         # 1.Find all gates (not empty room) and add them to the queue
#         for i in range(rows):
#             for j in range(columns):
#                 if rooms[i][j]==0:
#                     queue.append((i, j))
#         while queue:
#             x, y = queue.popleft()
#             for i, j in dir:
#                 new_x = x+i
#                 new_y = y+j
#                 # If the new cell is an empty room, update its distance and add it to the queue
#                 if (0<=new_x<rows and 0<=new_y<columns) and rooms[new_x][new_y]==2147483647:
#                     rooms[new_x][new_y]=rooms[x][y]+1
#                     queue.append((new_x, new_y))


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        dir = [(0,1),(1,0),(-1,0), (0, -1)]
        rows = len(rooms)
        columns = len(rooms[0])
        queue = deque()
        
        for i in range(rows):
            for j in range(columns):
                if rooms[i][j] ==0:
                    queue.append((i,j))
        while queue:
            x, y = queue.popleft()
            for i, j in dir:
                new_x = x+i
                new_y = y+j
                if (0<=new_x<rows and 0<=new_y<columns) and rooms[new_x][new_y]==2147483647:
                    rooms[new_x][new_y] = rooms[x][y]+1
                    queue.append( (new_x, new_y))
        
                                 

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        dir = [(0,1),(1,0),(-1,0), (0, -1)]
        rows = len(grid)
        columns = len(grid[0])
        queue = deque()
        visited = set()

        dist = [[float('inf')] * columns for _ in range(rows)]
        num_buildings_reached = [[0] * columns for _ in range(rows)]
        num_buildings = 0

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] ==1:
                    visited.add((i, j))
                    num_buildings+=1
                    queue.append((i,j,0))

        while queue:
            x, y, curDist = queue.popleft()
            for i, j in dir:
                new_x = x+i
                new_y = y+j
                if (0<=new_x<rows and 0<=new_y<columns) and (new_x, new_y) not in visited and grid[new_x][new_y] ==0:
                    dist[new_x][new_y]+= curDist+1
                    num_buildings_reached[new_x][new_y]+=1
                    queue.append( (new_x, new_y, curDist+1))
                    visited.add((new_x, new_y))
                    
            
        min_distance = float('inf')
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0 and num_buildings_reached[i][j] == num_buildings:
                    min_distance = min(min_distance, dist[i][j])    
        return min_distance if min_distance != float('inf') else -1

        



        


        

                    
                        
                    
                    
                    
            
                    

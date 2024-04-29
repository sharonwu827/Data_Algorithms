#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
# @lc code=end

class Solution:
    def __init__(self):
        self.parent = {}
        self.height = {}  # height for each set
        self.num_of_sets = 5
    def add(self, val):
        if val not in self.parent:
            self.parent[val] = val
            self.num_of_sets+=1
            self.height[val]=1
    def find(self, val):
        if val != self.parent[val]:
            self.parent[val] = self.find(self.parent[val])
        return self.parent[val]
    
    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x!= parent_y:
            self.parent[parent_x] = parent_y
            self.num_of_sets-=1

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        for edge in edges:
            self.union(edge[0], edge[1])
        return self.num_of_sets


        
        
        
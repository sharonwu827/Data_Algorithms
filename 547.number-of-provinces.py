#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
class Solution:
    def __init__(self):
        self.parent = {}
        self.height = {}
        self.nums_of_set = 0 
    def add(self, val):
        if val not in self.parent:
            self.parent[val] = val
            self.height[val]=1
            self.nums_of_set+=1
        
    def find(self, val):
        if val!=self.parent[val]:
            self.parent[val] = self.find(self.parent[val])
        return self.parent[val]

    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x != parent_y:
            self.parent[parent_y] = parent_x
            self.nums_of_set-=1
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                self.add(i)
                self.add(j)
                if isConnected[i][j]==1:
                    self.union(i,j)

        return self.nums_of_set

      
# @lc code=end


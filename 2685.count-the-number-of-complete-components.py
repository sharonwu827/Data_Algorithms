#
# @lc app=leetcode id=2685 lang=python3
#
# [2685] Count the Number of Complete Components
#

# @lc code=start

class UnionFind:
    def __init__(self, n):
        self.parents = {}
        self.sets = 0
    def add(self, val):
        if val not in self.parents:
            self.parents[val] = val
            self.sets+=1

    def find(self, val):
        if self.parents[val] != val:
            self.parents[val] = self.find(self.parents[val])
        return self.parents[val]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parents[root_x] = root_y
            self.sets-=1

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for i in range(n):
            uf.add(i)
        for edge in edges:
            uf.union(edge[0], edge[1])
        return uf.sets

        
# @lc code=end


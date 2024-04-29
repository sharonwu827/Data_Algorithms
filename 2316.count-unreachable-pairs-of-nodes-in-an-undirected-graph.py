#
# @lc app=leetcode id=2316 lang=python3
#
# [2316] Count Unreachable Pairs of Nodes in an Undirected Graph
#

# @lc code=start
class Solution:
    def __init__(self):
        self.parent = {}
        self.size = {}
        self.num_of_sets = 0
    def add(self, val):
        if val not in self.parent:
            self.parent[val]=val
            self.size[val]=1 #注意这里是self.size[val]=1 不是self.size[val]+=1 
            self.num_of_sets+=1
    def find(self, val):
        if self.parent[val]!=val:
            self.parent[val] = self.find(self.parent[val])
        return self.parent[val]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x!=root_y:
            self.parent[root_x] = root_y
            self.size[root_y]+=self.size[root_x]
            self.size[root_x]=0 #注意这里需要更改root_x的size
            self.num_of_sets-=1
        
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        for i in range(n):
            self.add(i)
        for edge in edges:
            self.union(edge[0], edge[1])

        # 计算总连接数减去每组内的权重
        total_size = n*(n-1)//2

        for i in self.size:
            total_size  -= self.size[i]*(self.size[i]-1)//2
        return total_size 

        
# @lc code=end


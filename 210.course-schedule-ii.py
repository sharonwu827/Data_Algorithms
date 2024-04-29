#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        list_ = [ [] for _ in range(numCourses)]
        for second, first in prerequisites:
            list_[second].append(first)
        visited = [0]*numCourses
        onPath = [0]*numCourses
        hasCycle = False
        res = []

        def dfs(n):
            nonlocal hasCycle
            if onPath[n]==1:
                hasCycle = True
                return
            if visited[n]==1:
                return 
            visited[n]=1
            onPath[n]=1
            for i in list_[n]:
                dfs(i)
            onPath[n]=0
            res.append(n)

        for i in range(numCourses):
            dfs(i)
            if hasCycle:
                return []
        return res
            

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        list_ = [ [] for _ in range(n)]
        for edge in edges:
            list_[edge[0]].append(edge[1])
            list_[edge[1]].append(edge[0])
        visited = [0]*n
        onPath = [0]*n
        self.hasCycle = False

        # add a prev parameter to keep track of the previously visited node. 
        # This avoid going back to the parent node and falsely detecting cycles.
        def dfs(n, prev):
            if onPath[n]==1:
                self.hasCycle=True
                return
            if visited[n]==1:
                return 
            visited[n]=1
            onPath[n]=1
            for i in list_[n]:
                if i!=prev:
                    dfs(i, n)
            onPath[n]=0

        # we dont need for loop here
        # If the graph is a valid tree, all nodes should be reachable from any starting node.
        dfs(0, -1)
          
        return not self.hasCycle and all(visited)
    

class UnionFind:
    def __init__(self, x, y):
        self.parent = {}
        self.height = {}
        self.num_of_sets = 0 
    def add(self,val):
        
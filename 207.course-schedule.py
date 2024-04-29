#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def buildAdjList(n):
            adj_list = [[] for _ in range(numCourses)]
            for i, j in prerequisites:
                adj_list[j].append(i)
            return adj_list
        
        adj_list = buildAdjList(numCourses)
        visited = [0] * numCourses
        onPath = [0] * numCourses
        hasCycle = False
        res = []
        def dfs(n):
            nonlocal hasCycle
            if onPath[n] == 1:
                hasCycle = True
                return
            if visited[n] == 1:
                return 
            visited[n] = 1
            onPath[n] = 1
            for i in adj_list[n]:
                dfs(i)
                res.append(i)
            onPath[n] = 0
        
        for i in range(numCourses):
            dfs(i)
            if hasCycle:
                return False  # Return False if cycle is detected
        return res
            
            

        


            
        

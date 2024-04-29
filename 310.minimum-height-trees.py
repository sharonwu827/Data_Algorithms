#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def buildAdjList(numCourses, prerequisites):
            adjlist = [[] for _ in range(numCourses)]
            for i, j in prerequisites:
                adjlist[i].append(j)
            return adjlist
        
        indegree = [0] * n
        for edge in edges:
            from_node, to_node = edge[1], edge[0]
            # 节点 to_node 的入度加一
            indegree[to_node] += 1
        queue = []
        for i in range(numCourses): 
            if indegree[i] == 0:
                queue.append(i)
            visited = 0
        


# @lc code=end



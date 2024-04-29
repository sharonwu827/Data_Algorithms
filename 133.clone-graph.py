#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        adjList = []
        def traverse(node, path):
           
            if not node:
                return
            path.append(node.copy())
            path.append(node.val)
            for i in node.neighbors:
                adjList[node.val-1].append(i)
            path.pop()
        
        for i in range(node.val-1):
            traverse(i, [])
            return

                



        
# @lc code=end


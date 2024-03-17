#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.max_depth = 0
        def dfs(node, depth):
            if not node:
                return 0
            if not node.children:
                self.max_depth = max(self.max_depth, depth)
            for child in node.children:
                dfs(child, depth+1)
        dfs(root, 1)
        return self.max_depth

        
# @lc code=end


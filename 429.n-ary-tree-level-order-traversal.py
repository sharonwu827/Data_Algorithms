#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        res = []
        while queue:
            tmp = []
            for _ in range(len(queue)):
                curNode = queue.pop(0)
                tmp.append(curNode.val)
                for child in curNode.children:
                    queue.append(child)
            res.append(tmp)
        return res
        
        
# @lc code=end


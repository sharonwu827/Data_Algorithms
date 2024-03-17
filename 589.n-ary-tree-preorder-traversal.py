#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
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
    def preorder(self, root: 'Node') -> List[int]:

        queue = [root]
        res = []
        while queue:
            for _ in range(len(queue)):
                cur = queue.pop(0)
                res.append(cur.val)
                for child in cur.children:
                    res.append(child.val)
                    queue.append(child)
        return res



     
# @lc code=end


#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque()
        queue.append((root, 1))
        while queue:
            for _ in range(len(queue)):
                cur, curDepth = queue.popleft()
                if not cur.left and not cur.right:
                    return curDepth
                if cur.left:
                    queue.append((cur.left, curDepth + 1))
                if cur.right:
                    queue.append((cur.right, curDepth + 1))
        return 0


            
            
# @lc code=end


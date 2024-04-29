#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = 0
        # get the height of the current node
        def dfs(root, depth):
            if not root:
                return 0
            left = dfs(root.left, depth+1)
            right = dfs(root.right, depth+1)
            if not root.left and not root.right:
                self.maxDepth = max(self.maxDepth, depth)
  
        dfs(root, 1)
        return self.maxDepth


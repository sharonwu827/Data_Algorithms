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
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.min_depth = float('inf')
        def dfs(node, depth):
            if not node:
                return 0
            if not node.left and not node.right:
                self.min_depth = min(self.min_depth, depth)
            left = dfs(node.left, depth+1)
            right = dfs(node.right, depth+1)
        
        if not root:
            return 0
        dfs(root, 1)
        return self.min_depth

        
# @lc code=end


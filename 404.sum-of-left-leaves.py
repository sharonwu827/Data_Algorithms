#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.res = 0 
        def dfs(node):
            if not node:
                return 0
            if node.left and not node.left.left and not node.left.right:
                self.res+=node.left.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.res

        
# @lc code=end


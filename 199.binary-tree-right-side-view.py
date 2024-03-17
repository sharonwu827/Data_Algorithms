#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverse(node):
            if not node:
                return 
            if node.left and node.right:
                traverse(node.right)
            if not node.right and node.left:
                traverse(node.left)
            
                        
            
# @lc code=end


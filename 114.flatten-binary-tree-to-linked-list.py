#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(root: TreeNode) -> None:
        def helper(node):
            if not node:
                return 
            left = node.left
            right = node.right

            node.right = node.left
            node.right.right = right

            helper(node.left)
            helper(node.right)
        helper(root)
        return root
            

       

        
# @lc code=end


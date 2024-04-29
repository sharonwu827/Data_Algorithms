#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       
       def helper(node, low, high):
           if not node:
               return True
           if node.val <= low or node.val >= high:
               return False
           left = helper(node.left, low, node.val)
           right = helper(node.right, node.val, high)
           return left and right
       return helper(root, float("-inf"),float("inf"))
            
        
# @lc code=end


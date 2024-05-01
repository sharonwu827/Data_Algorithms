#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val<key:
            root.right = self.deleteNode(root.right, key)
        if root.val>key:
            root.left = self.deleteNode(root.left, key)
        
        if root.val==key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # find 右子树最小值
            tmp = root.right
            while tmp.left:
                tmp = tmp.left
            root.val = tmp.val
            root.right = self.deleteNode(root.right, tmp.val)
        
        return root
            

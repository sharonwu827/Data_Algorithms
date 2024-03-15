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
        # base case
        if not root:
            return
        # 利用定义，把左右子树拉平
        flatten(root.left)
        flatten(root.right)
        
        # 后序遍历位置
        # 1、左右子树已经被拉平成一条链表
        left = root.left
        right = root.right
        # 2、将左子树作为右子树
        root.left = None
        root.right = left
        
        # 3、将原先的右子树接到当前右子树的末端
        p = root
        while p.right:
            p = p.right
        p.right = right

        
# @lc code=end


#
# @lc app=leetcode id=965 lang=python3
#
# [965] Univalued Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        value_ = root.val if root else None  # Handle the case when root is None

        # def PreOrder(node):
        #     if not node: 
        #         return True
            
        #     if node.val != value_:
        #         return False
            
        #     return PreOrder(node.left) and PreOrder(node.right)

        # return PreOrder(root)
        # def Inorder(node):
        #     if not node:
        #         return True
        #      # 先遍历左子树
        #     left_res = Inorder(node.left)
        #     # ensure that the left subtree is a uni-valued tree 
        #     # before checking the current node and the right subtree.
        #     if left_res is False:
        #         return False
        #     if node.val!=value_:
        #         return False
        #     right_res = Inorder(node.right)
        #     return right_res
        # return Inorder(root)


        # def Postorder(node):
        #     if not node:
        #         return True
        #     left_res = Postorder(node.left)
        #     right_res = Postorder(node.right)
        #     if node.val!=value_:
        #         return False
        #     return left_res and right_res
        # return Postorder(root)
        
        def recursion(node):
            if not node:
                return True
            if node.val!=value_:
                return False
            return recursion(node.left) and recursion(node.right)
        
        return recursion(root)

# @lc code=end


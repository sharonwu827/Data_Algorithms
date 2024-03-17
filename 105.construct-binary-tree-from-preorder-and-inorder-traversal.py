#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_index = {val:i for i, val in enumerate(inorder)}
        
        def mybuildTree(preleft, preright, inleft, inright):
            if preleft > preright or inleft>inright:
                return 
            
            #current root val, the first element on the preorder list
            root_val = preorder[preleft]
            root = TreeNode(root_val)
            
            # 此时root在inorder的index
            in_root_ind = inorder_index[root_val]
            
            # get left tree length from inorder 
            left_tree_length = in_root_ind  -1 - inleft
            
            # get index of where left tree ends in preorder
            pre_left_ind = preleft+1+left_tree_length
            
            root.left = mybuildTree(preleft+1, pre_left_ind, inleft, in_root_ind -1)
            root.right = mybuildTree(pre_left_ind+1, preright, in_root_ind+1, inright)
            
            return root
            
        return mybuildTree(0, len(preorder)-1, 0, len(inorder)-1)
# @lc code=end


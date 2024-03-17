#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = rightclass Solution:
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val:i for i, val in enumerate(inorder)}
        
        def mybuildTree(inleft, inright, postleft, postright):
            if inleft > inright or postleft > postright:
                return 
            
            #current root val, the last element on the postorder list
            root_val = postorder[postright]
            root = TreeNode(root_val)
            
            # 此时root在inorder的index
            in_root_ind = inorder_index[root_val]
            
            # get left tree length from inorder 
            left_tree_length = in_root_ind  -1 - inleft
            
            # get index of where left tree ends in preorder
            post_left_ind = postleft+left_tree_length
            
            root.left = mybuildTree(inleft, in_root_ind-1, postleft,  post_left_ind)
            root.right = mybuildTree(in_root_ind+1, inright,  post_left_ind+1, postright-1)
            
            return root
            
        return mybuildTree(0, len(inorder)-1, 0, len(postorder)-1)
    
# @lc code=end


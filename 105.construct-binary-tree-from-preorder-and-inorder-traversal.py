#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def buildTreeHelper(pstart, pend, istart, iend):
            if pend < pstart or iend <  istart:
                return
            root_val = preorder[pstart]
            root = TreeNode(root_val)
            ind = inorder.index(root_val)

            left_tree_len = ind-1-istart
            left_tree_pind = ind-istart+pstart

            root.left = buildTreeHelper(pstart+1,left_tree_pind, istart, ind-1)
            root.right = buildTreeHelper(left_tree_pind+1, pend, ind+1, iend)
            return root
        return buildTreeHelper(0, len(preorder)-1, 0, len(inorder)-1)

            

# @lc code=end


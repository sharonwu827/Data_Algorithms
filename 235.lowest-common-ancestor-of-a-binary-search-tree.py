#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minVal = min(p.val, q.val)
        maxVal = max(p.val, q.val)
        if root.val == minVal or root.val == maxVal or minVal<root.val<maxVal:
            return root
        if root.val>maxVal:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val<minVal:
            return self.lowestCommonAncestor(root.right, p, q)
        


        

# @lc code=end


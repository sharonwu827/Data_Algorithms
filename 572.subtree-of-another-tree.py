#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p1, p2):
            if not p1 and not p2:
                return True
            if not p1 or not p2:
                return False
            if p1.val!=p2.val:
                return False
            return sameTree(p1.left, p2.left) and sameTree(p1.right, p2.right)
        
        def dfs(p1, p2):
            if not p1 and not p2:
                return False
            if not p1 or not p2:
                return False
            if sameTree(p1, p2) is True:
                return True
            
            return dfs(p1.left, p2) or dfs(p1.right, p2) 
        
        return dfs(root, subRoot)     
# @lc code=end


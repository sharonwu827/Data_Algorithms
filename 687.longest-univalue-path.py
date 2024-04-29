#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.longestPath = 0 
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if root.left:
                if root.left.val == root.val:
                    left+=1
                else:
                    left=0
            if root.right:
                if root.right.val == root.val:
                    right+=1
                else:
                    right=0
            self.longestPath = max(self.longestPath, left+right)
            return max(left, right)
        dfs(root)
        return self.longestPath
            
      
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if not p or not q:
            return 
        if p.parent == q.parent:
            return p.parent
        if p.parent == q:
            return q
        if q.parent == p:
            return p
        left = self.lowestCommonAncestor(p, q)
        right = self.lowestCommonAncestor(p,q)


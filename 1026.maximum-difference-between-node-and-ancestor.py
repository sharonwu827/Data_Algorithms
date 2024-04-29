#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def getAncestor(root):
            if not root:
                return 
            
  
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if not p.parent or not q.parent:
            return
        if p.parent == q:
            return q
        if q.parent == p:
            return p   
        if q.parent == p.parent:
            return p.parent
        return self.lowestCommonAncestor(p.parent, q.parent)

        
# @lc code=end



class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':





class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.isPExist = False
        self.isQExist = False
        def getAncestor(root, p, q):
            if not root:
                return 
            if root.val == p.val:
                self.isPExist = True
            if root.val == q.val:
                self.isQExist = True
            left = getAncestor(root.left, p, q)
            right = getAncestor(root.right, p, q)
            if root.val == p.val or root.val == q.val:
                return root
            if left and right:
                return root
            if left:
                return left
            if right:
                return right
        
        res = getAncestor(root, p, q)
        if not is_p_existed or not is_q_existed:
            return None
        else:
            return res
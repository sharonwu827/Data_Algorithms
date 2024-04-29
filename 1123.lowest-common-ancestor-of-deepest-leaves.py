#
# @lc app=leetcode id=1123 lang=python3
#
# [1123] Lowest Common Ancestor of Deepest Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def getAncestor(root, nodes):
            if not nodes or not root:
                return 
            # if root in nodes:
            #     return root
            for node in nodes:
                if root.val == node.val:
                    return root
            left = getAncestor(root.left, nodes)
            right = getAncestor(root.right, nodes)
            if left and right:
                return root
            if left:
                return left
            if right:
                return right
            
        def getDeepestLeaves(root):
            queue = deque()
            queue.append(root)
            deepestLeaves = []
            while queue:
                tmp = []
                for _ in range(len(queue)):
                    cur = queue.popleft()
                    tmp.append(cur)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                deepestLeaves =  tmp
            return deepestLeaves
        
        deepestLeaves = getDeepestLeaves(root)
        return getAncestor(root,deepestLeaves) 

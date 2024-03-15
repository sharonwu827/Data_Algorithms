#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def bfs(root):
            if not root:
                return 
            queue = [root]
            res = []
            while queue:
                for _ in range(len(queue)):
                    cur = queue.pop()
                    if not cur.left and not cur.right:
                        res.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
            return res
        return bfs(root1) == bfs(root2)

            
        
# @lc code=end


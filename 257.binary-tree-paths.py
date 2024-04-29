#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []
        self.path = []
        def traverse(node):
            if not node:
                return 
            
            self.path.append(str(node.val))
            if not node.left and not node.right:
                self.res.append("->".join(self.path))
            traverse(node.left)
            traverse(node.right)
            self.path.pop()
        traverse(root)
        return self.res
        
            

   

      
# @lc code=end


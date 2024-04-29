#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0 
        self.path = 0
        def traverse(node):
            if not node:
                return 
            self.path = (self.path << 1) | root.val
            if not node.left and not node.right:
                self.res += (self.path << 1) | root.val
            traverse(node.left)
            traverse(node.right)
            self.curPath.pop()
        traverse(root)
        return self.res


            

        
# @lc code=end


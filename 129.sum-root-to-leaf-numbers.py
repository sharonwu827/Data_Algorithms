#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.curSum = 0 
        def traverse(node):
            if not node:
                return 
            self.curSum = self.curSum * 10 + node.val
            if not node.left and not node.right:
                self.res += self.curSum
            traverse(node.left)
            traverse(node.right)
            self.curSum = (self.curSum - node.val)//10

        traverse(root)
        return self.res

        
# @lc code=end


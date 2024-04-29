#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = []
        self.tmp = []
        self.prev = None
        def traverse(root):
            if not root:
                return 

            if self.prev and root.val-self.prev==1:
                self.tmp.append(root.val)
                if len(self.tmp)>len(self.res):
                    self.res = self.tmp
            self.prev = root.val

            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return self.res
            

        
# @lc code=end


#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diamter = 0 
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            # at current node
            # get its longest path which is left+right
            # and compare it with self.diameter
            self.diamter = max(left+right, self.diamter)
            # return the longest path at node
            return max(left, right)+1 
        dfs(root)
        return self.diamter

        
# @lc code=end


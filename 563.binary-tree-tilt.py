#
# @lc app=leetcode id=563 lang=python3
#
# [563] Binary Tree Tilt
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return 0 
            left = dfs(root.left)
            right = dfs(root.right)
            # calculate each root tilt while traverse
            self.res+=abs(right-left)
            # computing the sum of values in the subtree rooted at the current node
            # This sum is needed because we want to calculate the tilt of the current node based on the sum of values in its left and right subtrees.
            return left+right+root.val
        dfs(root)
        return self.res
        
        
# @lc code=end


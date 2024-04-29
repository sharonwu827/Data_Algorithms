#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -float("inf")
        def dfs(node):
            if not node:
                return 0
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            self.max_sum = max(self.max_sum, left_max+right_max+node.val)
            return node.val+max(left_max, right_max)
        dfs(root)
        return self.max_sum
            



        
# @lc code=end


#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.curSum = 0 
        def dfs(node):
            if not node:
                return False
            self.curSum+=node.val
            if not node.left and not node.right:
                if self.curSum == targetSum:
                    return True
            dfs(node.left)
            dfs(node.right)
            self.curSum-=node.val
            return False

        if not root:
            return False
        return dfs(root) 

            
          
# @lc code=end


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
        def hasPathSum(root, curSum):
            if not root:
                return False
            curSum+=root.val
            if not root.left and not root.right:
                if curSum == targetSum:
                    return True
            left = hasPathSum(root.left, curSum)
            right = hasPathSum(root.right, curSum)
            # curSum-=root.val!!! we dont need it
            # 为什么要返回left or right
            # if left subtree or right subtree return true, then we find a path
            return left or right
        return hasPathSum(root, 0)
        



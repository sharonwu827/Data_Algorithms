#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(node1, node2):
            if not node1 and not node2:
                return True
            left_res = traverse(node1.left, node2.left)
            if not left_res:
                return False
            right_res = traverse(node1.right, node2.right)
            if not right_res:
                return False
        return traverse(p, q)
            


        
# @lc code=end


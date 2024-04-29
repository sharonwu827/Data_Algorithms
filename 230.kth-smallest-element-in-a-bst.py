#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.rank = 0 
        def traverse(root,k):
            if not root:
                return
            traverse(root.left, k)
            self.rank+=1
            if self.rank == k:
                self.res = root.val
            traverse(root.right, k)
        traverse(root, k)
        return self.res
        

        

        

    
# @lc code=end


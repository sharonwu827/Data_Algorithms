#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(nums):
            if not nums:
                return 
            max_val = max(nums)
            max_ind = nums.index(max_val)
            root = TreeNode(max_val)
            left = buildTree(nums[:max_ind])
            right = buildTree(nums[max_ind+1:])
            root.left = left
            root.right = right
            return root
        return buildTree(nums)
            
           
# @lc code=end


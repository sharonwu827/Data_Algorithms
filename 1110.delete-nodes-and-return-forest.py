#
# @lc app=leetcode id=1110 lang=python3
#
# [1110] Delete Nodes And Return Forest
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        delete = []
        def dfs(node, path):
            if not node:
                return 
            if node.val in to_delete:
                delete = node.val 
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if delete:
                return None
            else:
                if is_root

            
                


        
        
# @lc code=end


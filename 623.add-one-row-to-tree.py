#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # dfs return the node after modifiation
        def dfs(node, curdepth):
            if not node:
                return 
            if curdepth == depth-1:
                tmp_left = node.left
                tmp_right = node.right
                node.left = TreeNode(val)
                node.right = TreeNode(val)
                node.left.left = tmp_left
                node.right.right = tmp_right
            node.left = dfs(node.left, curdepth+1)
            node.right = dfs(node.right, curdepth+1)
            return node
        
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        return dfs(root, 1)

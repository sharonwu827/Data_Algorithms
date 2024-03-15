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
        self.diameter = -float('inf')
        def dfs(node):
            if not node:
                return 0
            left_diameter = dfs(node.left)
            right_diameter = dfs(node.right)
            self.diameter = max(self.diameter, left_diameter + right_diameter)
            return max(left_diameter,  right_diameter)+1
        dfs(root)
        return self.diameter
            


# def traverse(node, level)
#     if not node:
#         return 0 
#     print(f"节点 {node} 在第 {level} 层")
#     traverse(node.left, level + 1)
#     traverse(node.right, level + 1)


# def traverse(node, level)
#     if not node:
#         return 0 
#     left_level = traverse(node.left, level + 1)
#     right_level = traverse(node.right, level + 1)
#     print(f"节点 {node}的左边子树在第 {left_level} 层，右边子树 在第 {right_level} 层")
#     return left_level + right_level + 1

        
# @lc code=end


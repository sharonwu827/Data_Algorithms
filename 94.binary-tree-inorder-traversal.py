#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        curNode = root
        res = []
        while stack or curNode:
            while curNode:
                stack.append(curNode)
                curNode = curNode.left
            else:
                curNode = stack.pop()
                res.append(curNode.val)
                curNode = curNode.right
        return res

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        curNode = root
        res = []
        while stack or curNode:
            while curNode:
                stack.append(curNode)
                res.append(curNode.val)
                curNode = curNode.left
            else:
                curNode = stack.pop()
                curNode = curNode.right
        return res

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        curNode = root
        res = []
        while stack or curNode:
            while curNode:
                stack.append(curNode)
                res.append(curNode.val)
                curNode = curNode.right
            else:
                curNode = stack.pop()
                curNode = curNode.left
        return res[::-1]



        
        
# @lc code=end


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
        stack = []
        curNode = root

        while stack or curNode:
            while curNode:
                stack.append(curNode)
                curNode = curNode.left
            else:
                curNode = stack.pop()
                k-=1
                if k==0:
                    return curNode.val
                curNode = curNode.right




        

        

    
# @lc code=end


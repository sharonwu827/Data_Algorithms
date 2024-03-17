#
# @lc app=leetcode id=1367 lang=python3
#
# [1367] Linked List in Binary Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def isSame(node, p):
            if not p:
                return True
            if not node:
                return False
            return node.val == p.val and (isSame(node.left, p.next) or isSame(node.right, p.next))
        
        if not root:
            return False
        return isSame(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

            
# @lc code=end


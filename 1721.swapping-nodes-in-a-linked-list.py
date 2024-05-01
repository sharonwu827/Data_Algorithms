#
# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head, k):
        cur = head
        for i in range(k-1):
            cur = cur.next
        left = cur
        right = head
        while cur.next:
            cur =  cur.next
            right = right.next
        
        left.val, right.val = right.val, left.val
        return head



        
        # @lc code=end


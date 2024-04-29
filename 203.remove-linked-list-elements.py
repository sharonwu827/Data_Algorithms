#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        p = dummy 
        while p and p.next:
            while p.next and p.next.val == val:
                p.next = p.next.next
            p = p.next
        return dummy.next
                

        
        
# @lc code=end


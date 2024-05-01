#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check for edge cases
        if not head or k == 0:
            return head

        # Compute the length of the linked list
        n = 0 
        p = head
        while p:
            n+=1
            p=p.next

        p1 = head
        p2 = head
        if k%n==0:
            return head
        
        for _ in range(k%n):
            p2 = p2.next

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next
        
        tmp = p1.next 
        p1.next = None
        p = tmp

        while p.next:
            p = p.next
        p.next = head
        return tmp
# @lc code=end


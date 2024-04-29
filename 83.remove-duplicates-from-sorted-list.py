#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        dummy.next = head
        p = dummy
        while p and p.next:
            while p.next and p.val==p.next.val:
                p.next = p.next.next
            p=p.next
        return dummy.next

# @lc code=end


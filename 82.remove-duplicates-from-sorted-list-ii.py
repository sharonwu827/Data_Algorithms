#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        p = dummy
        while p.next and p.next.next:
            while p.next.val == p.next.next.val:
                p.next = p.next.next
            p = p.next
        return dummy.next

        
# @lc code=end


#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def getMid(head):
            p1 = head
            p2 = head
            while p2.next and p2.next.next:
                p1 = p1.next
                p2 = p2.next.next
            return p1 # the end of first half 
        
        def reverseLink(head, tail):
            prev = None
            cur = head
            while cur!=tail:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        mid = getMid(head)
        
        return reverseLink(head, mid) == mid


        
# @lc code=end


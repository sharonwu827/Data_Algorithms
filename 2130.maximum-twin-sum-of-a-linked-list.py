#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def partition(head):
            p1 = head
            p2 = head
            while p2.next and p2.next.next:
                p1 = p1.next
                p2 = p2.next.next
            right = p1.next
            p1.next = None
            left = head
            return left, right # return the right sub list
        def reverseLinkList(head):
            prev = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        left, right = partition(head)
        reversedRight = reverseLinkList(right)
        p1 = left
        p2 = reversedRight
        maxSum = 0 
        while p1 and p2:
            maxSum = max(maxSum, p1.val+p2.val)
            p1 = p1.next
            p2 = p2.next
        return maxSum
            
     
# @lc code=end


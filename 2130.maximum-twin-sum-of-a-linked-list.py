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
        def getMid(head):
            p1 = head
            p2 = head
            while p2.next and p2.next.next:
                p1 = p1.next
                p2 = p2.next.next
            return p1
        mid = getMid(head)
        secondHalfHead = mid.next
        mid.next = None
        firstHalf = head

        def reverseLinkedList(prev, head):
            cur = head
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev # not return cur.next cuz cur is none
        reversedSecondHalf = reverseLinkedList(None, secondHalfHead)
        maxTwinSum = 0
        p1 = firstHalf
        p2 = reversedSecondHalf
        while p1 and p2:
            maxTwinSum = max(maxTwinSum, p1.val+p2.val)
            p1 = p1.next
            p2 = p2.next
        return maxTwinSum
    

    
            
     
# @lc code=end


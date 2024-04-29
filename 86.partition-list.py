#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(None)
        dummy2 = ListNode(None)
        p1, p2 = dummy1, dummy2
        p = head
        while p:
            if p.val>=x:
                p2.next = p
                p2 = p2.next

            else:
                p1.next = p
                p1 = p1.next
            # 不能直接让 p 指针前进，
            # p = p.next
            # 断开原链表中的每个节点的 next 指针
            tmp = p.next
            p.next = None
            p = tmp
        p1.next = dummy2.next
        return dummy1.next
                


        
# @lc code=end


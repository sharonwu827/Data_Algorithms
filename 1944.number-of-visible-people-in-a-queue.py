#
# @lc app=leetcode id=1944 lang=python3
#
# [1944] Number of Visible People in a Queue
#

# @lc code=start
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
# @lc code=end

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode
        prev = head
        cur = head.next
        needInsert = True
        while needInsert:
            if prev.val <=insertVal and insertVal<=cur.val:
                needInsert =  False
            # means we find the position of the tail node
            # since the nodes are sorted in ascending order
            # the tail node would have the greatest value of all nodes
            if prev.val > cur.val:
                if insertVal >= prev.val or insertVal <= cur.val:
                    needInsert =  False
        
            if not needInsert:
                prev.next = Node(insertVal, cur)
                return head

            prev = prev.next
            cur = cur.next
            
            # loop condition
            if prev == head:
                break
        # did not insert the node in the loop
        prev.next = Node(insertVal, cur)
        return head
                



        
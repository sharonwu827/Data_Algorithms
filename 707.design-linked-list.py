#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start
class ListNode:
    def __init__(self, val = None):
        self.val = val
        self.next = None
        self.prev = None
class MyLinkedList:
    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        p = self.head
        while p:
            p = p.next
            index-=1
        return -1 if index else p.val
    
    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        self.head.next.prev = node
        self.head = node

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        node.next = None
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail = node
        
    def addAtIndex(self, index: int, val: int) -> None:
        
        

    def deleteAtIndex(self, index: int) -> None:

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end


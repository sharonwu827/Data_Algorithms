#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start

class LinkedList(self):
    def __init__(self):
        self.val = val 
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.dummy = LinkedList()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 and self.size >= index:
            return -1
        
        p = self.dummy.next

        for _ in range(index):
            p = p.next
        return p.val 

    def addAtHead(self, val: int) -> None:
        p = self.dummy
        p.next = 
        

    def addAtTail(self, val: int) -> None:
        

    def addAtIndex(self, index: int, val: int) -> None:
        

    def deleteAtIndex(self, index: int) -> None:
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end


#
# @lc app=leetcode id=1472 lang=python3
#
# [1472] Design Browser History
#

class DoubleLinkedList:
    def __init__(self, key = None, val = None):
        self.key = None
        self.val = None
        self.next = None
        self.prev = None
# @lc code=start
class BrowserHistory:

    def __init__(self, homepage: str):
        node = DoubleLinkedList(val = homepage)
        self.head = DoubleLinkedList()
        self.tail = DoubleLinkedList()
        self.head.next = node
        node.prev = self.head
        self.tail.prev = node
        node.next = self.tail
        self.pos = node

    def visit(self, url: str) -> None:
        node = DoubleLinkedList(val = url)
        self.addNodeToTail(node)
        self.pos = node

    def back(self, steps: int) -> str:
        while self.pos and steps:
            self.pos = self.pos.prev
            steps-=1
        if steps:
            self.pos = self.head.next
        return self.pos.val      
        
    def forward(self, steps: int) -> str:
        while self.pos and steps:
            self.pos = self.pos.next
            steps-=1
        if steps:
            self.pos = self.tail.prev
        return self.pos.val

    def addNodeToTail(self, node):
        listToRemove =  self.pos.next 
        listToRemove.prev = None
        node.prev = self.pos
        self.pos.next = node
        self.tail.prev = self.node
        self.node.next = self.tail


        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end

class HitCounter:

    def __init__(self):
        self.hits = deque()
        
    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        
    def getHits(self, timestamp: int) -> int:
        if self.hits and timestamp-self.hits[0]>=300:
            self.hits.popleft()
        return len(self.hits)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class MaxStack:

    def __init__(self):
        self.

    def push(self, x: int) -> None:
        
        

    def pop(self) -> int:
        

    def top(self) -> int:
        

    def peekMax(self) -> int:
        

    def popMax(self) -> int:
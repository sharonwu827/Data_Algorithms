#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#


# @lc code=start
class DoubleLinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head = DoubleLinkedList()
        self.tail = DoubleLinkedList()
        self.head.next = self.tail
        self.tail.pre = self.head
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # if key exists
        # we need to move the node to the head of list
        node = self.cache[key]
        self.moveToHead(node)
        return node.val
    def put(self, key, val):
        if key not in self.cache:
            node = DoubleLinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(val)
            self.size+=1
            if self.size>=self.capacity:
                removed = self.removeNode()
                self.cache.pop(removed.key)
                self.size-=1
        else:
            node = self.cache[key]
            node.value = val
            self.moveToHead(node)
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def addToHead(self, node):
         # add the most recent used node to head
        self.head.next.prev = node
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

                        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x:x[-1])
        for i in range(1, len(intervals)):
            if intervals[i-1][-1]>intervals[i][0]:
                return False
        return True
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Sort intervals based on start times
        # cannot sort based on end time
        # need to consider the meetings in chronological order based on their start times.
        intervals.sort(key = lambda x:x[0])
        # adding the meeting ending time
        minHeap=[] 
        heapq.heappush(minHeap, intervals[0][1])
        roomsNeed=1
        for i in range(1, len(intervals)):
            # A new meeting starts before any existing meeting ends, so a new room is needed
            if intervals[i][0]<minHeap[0]:
                roomsNeed+=1
            else: # can use the free room
                heapq.heappop(minHeap)

            heapq.heappush(minHeap, intervals[i][1])

        return roomsNeed

#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        

        
# @lc code=end   


class StringIterator:

    def __init__(self, compressedString: str):
        self.strs = compressedString
        

    def next(self) -> str:
        i = 0 
        n = len(self.strs)
        while i<n:
            
    def hasNext(self) -> bool:

        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()






class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                curLen = 1
                while num+curLen in nums:
                    curLen+=1
                    maxLen = max(curLen, maxLen)
                    num = num+curLen
        return maxLen


                

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowVal, colVal, boxVal = defaultdict(set), defaultdict(set), defaultdict(set)
        for i in range(9):
            for j in range(9):
                curVal = board[i][j]
                if curVal in rowVal[i]:
                    return False
                if curVal in colVal[j]:
                    return False
                if curVal in boxVal[(i//3, j//3)]:
                    return False
                rowVal[i].add(curVal)
                colVal[j].add(curVal)
                boxVal[(i//3, j//3)].add(curVal)
        return True






class DoubleLinkList:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None        

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DoubleLinkList()
        self.tail = DoubleLinkList()
        self.cache = defaultdict() #store (key, node)
        self.frequency = defaultdict() #store (key, frequency)
        self.size = 0 # need this one to track the current size
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.frequency[key]+=1
            return node.val #注意不是return self.cache[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.frequency[key]+=1
        else:
            node = DoubleLinkList(key, value)
            self.cache[key] = node
            self.moveToHead(node)
            self.size+=1
            if self.size > self.capacity:
                node_to_remove = self.removeFromTail()
                del self.cache[node_to_remove.key]
                self.size -= 1
        
    def removeNode(self, node):
        tmp = node.prev
        tmp.next = node.next
        node.next.prev = tmp
    
    def moveToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    def insertNode(self, node):
        if 

    def removeFromTail(self):
        removed_node = self.tail.prev
        self.removeNode(removed_node)
        return removed_node
        


        

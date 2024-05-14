#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#

# @lc code=start
class DoubleLinkedList:
    # 提高访问属性的速度，并节省内存
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.freq = 1
        self.next = None
        self.prev = None

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = defaultdict() # (key, node)
        # 存储使用频率相同的缓存节点的双向链表
        self.freq = defaultdict(LinkedList) # key是freq,val是链表【代表收纳这一条链表】

        self.head = DoubleLinkedList()
        self.tail = DoubleLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        '''
        Gets the value of the key if the key exists in the cache. 
        '''
        if key in self.cache:
            node = self.cache[key]
            # prev Linked list that have the same freq
            # and remove node from the prev linked list
            prevFreq = node.freq
            prevLL =  self.freq[prevFreq] 
            prevLL.removeNode(node)
            # 然后频率+1，在新频率中插入
            node.freq+=1
            self.freq[node.freq].addToHead(node)
            # 如果之前的频率是最小值，且跨频率更新之后原频率列表为空，则更新最小频率
            if node.freq == self.minFreq+1 and len(self.freq[self.minFreq]) == 0:
                self.minFreq = node.freq
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            prevFreq = node.freq
            prevLL =  self.freq[prevFreq] 
            prevLL.removeNode(node)
            node.freq+=1
            self.freq[node.freq].addToHead(node)

        else:
            if len(self.cache)>=self.capacity:
                self.removeNode(self.tail.prev)
            node = DoubleLinkedList(value)
            self.addNode(node)
            self.cache[key] = node

    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next, node.prev = None, None
        return node
    
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def getNode(self, key):
        if key not in self.cache:  
            return 
        else:
            node = self.cache[key] 
            self.removeNode(node)  
            linkedList = self.freq[node.freq]
            if not linkedList.prev:  # 抽出来后，这摞书是空的
                del self.freq[node.freq]  # 移除空链表
            if self.min_freq == node.freq:  # 这摞书是最左边的
                self.min_freq += 1
        node.freq += 1  # 看书次数 +1
        self.addToHead(self.freq[node.freq], node) 
        return node

            
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


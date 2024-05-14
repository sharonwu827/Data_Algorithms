#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache

from collections import defaultdict

class DoubleLinkedList:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        # self.cache store key:node
        # node has key-value pair
        self.cache = defaultdict()
        self.head = DoubleLinkedList()
        self.tail = DoubleLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.add_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            #  Update the value of the key if the key exists.
            node.value = value
            # move the most recently used node to head
            self.remove_node(node)
            self.add_to_head(node)
        else:
            node = DoubleLinkedList(key, value)
            self.cache[key] = node
            self.add_to_head(node)
            self.size += 1
            # remove the LRU
            if self.size > self.capacity:
                node_to_remove = self.remove_node(self.tail.prev)
                del self.cache[node_to_remove.key]
                self.size -= 1

    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        return node



#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0 
        self.preCount = 0 
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node.preCount+=1
            node = node.children[char]
        node.count+=1
        

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char=='.':

            if char not in node.children and char != '.':
                return False
            node = node.children[char]
        return True
        


#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start


class TrieNode:
    def __init__(self):
        self.count = 0 # 表示以该处节点构成的单词的个数
        self.preCount = 0 # 表示以该处节点构成的前缀的字串的个数
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word): # 将单词（words）全部依次插入到前缀树中
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.preCount += 1 # why do we need this 
        node.count += 1

    def search(self, word): # if the word is in trie
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        # whether the count of the node representing the last character of the word > zero
        return node.count > 0

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.preCount > 0
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end


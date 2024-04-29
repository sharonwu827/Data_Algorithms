#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start

class WordDictionary:

    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = char
        node.isEndOfWord = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char == '.':
                continue
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEndOfWord # # 返回是否有单词结束标志
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end


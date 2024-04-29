#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir = [(0, 0), (0, 1), (-1, 0), (1, 0)]
        rows = len(board)
        cols = len(board[0])
        visited = set()
        def backtrack(x, y, i):
            if not (0<=x<rows and 0<=y<cols):
                return
            if i == len(word):
                return True
           
            if board[x][y] == word[i]:
                for i, j in dir:
                    new_x = x+i
                    new_y = y+j
                path.append(board[new_x][new_y])
                backtrack(new_x, new_y, path)
            visited.remove((x,y))
            path.pop()
        
        for x in range(rows):
            for y in range(cols):
                if board[x][y] == word[0]:
                    if backtrack(x, y, []):
                        return True
        return False



        
# @lc code=end

class Node:
    def __init__(self):
        # is_word表示这个结点是否为一个单词的结尾
        # next[]表示这个结点的下一个26个字母结点
        self.is_word = False
        self.next = [None]*26
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        now = self.root
        length = len(word)
        for i in range(length):
            # 依次查找每个字符
            # 如果所有下一个结点中没有当前字符，则增加新结点到下一个next[pos]
            pos = ord(word[i]) - ord('a')
            if now.next[pos] is None:
                now.next[pos] = Node()
            now = now.next[pos]
        now.is_word = True
    def search(self, word):
        now = self.root
        n = len(word)
        for i in range(n):
            
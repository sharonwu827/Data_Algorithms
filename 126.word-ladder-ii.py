#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordListSet = set(wordList)
        if beginWord in wordListSet:
            wordListSet.remove(beginWord)
        queue = deque()
        queue.append((beginWord, [beginWord]))
        res = []
        minPath = float('inf')
        while queue:
            word, path = queue.popleft()
            if word == endWord:
                if minPath > len(path):
                    res = [path]
                    minPath = len(path)
                elif minPath == len(path):
                    res.append(path) 
                
            for i in range(len(word)):
                for j in range(26): # Try all possible characters ('a' to 'z')
                    newWord = word[:i] + chr(ord('a') + j) + word[i+1:]
                    if newWord in wordListSet:
                        # Create a new path list instead of modifying the existing one
                        new_path = path + [newWord]
                        queue.append((newWord, new_path))
                        wordListSet.remove(newWord)
        return res
        
        
# @lc code=end


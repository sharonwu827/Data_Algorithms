#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordListSet = set(wordList)
        if beginWord in wordListSet:
            wordListSet.remove(beginWord)
        queue = deque[]
        queue.append((beginWord, 1))
        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordListSet:
                        queue.append((newWord, level+1))
                        wordListSet.remove(newWord)
        return 0
    

        

        
# @lc code=end


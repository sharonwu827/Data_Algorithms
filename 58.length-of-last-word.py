#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        wordCnt = 0 
        p = n-1
        while p >=0:
            while not s[p].isalnum():
                p-=1
            wordCnt+=1
            p-=1
            if not s[p].isalnum():
                break
        return wordCnt



        
# @lc code=end


#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        def backtrack(startInd, path):
            if startInd == len(s): # not startInd == len(s)-1
                res.append(' '.join(path))
                return 
            for i in range(startInd, len(s)):
                word = s[startInd:i+1]
                if word in wordDict:
                    backtrack(i+1, path + [word])
        backtrack(0, [])
        return res
                


# @lc code=end


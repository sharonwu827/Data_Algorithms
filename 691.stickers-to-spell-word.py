#
# @lc app=leetcode id=691 lang=python3
#
# [691] Stickers to Spell Word
#

# @lc code=start
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        res = float("inf")
        def backtrack(startInd, path):
            for i in range(startInd, len(stickers)):
                if stic
                backtrack(path)
        
# @lc code=end


#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dct = {va: i for i, va in enumerate(order)}
        pre = [dct[w] for w in words[0]]
        for word in words[1:]:
            cur = [dct[w] for w in word]
            if pre > cur:
                return False
            pre = cur
        return True


# @lc code=end


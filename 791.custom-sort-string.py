#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#

# @lc code=start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        frequency = Counter(s)
        res = []
        for char in order:
            if char in frequency:
                res.extend(char * frequency[char])
                del frequency[char]
        for char, freq in frequency.items():
            res.extend(char * freq)
        return ''.join(res)




# @lc code=end


#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictS = Counter(s)
        dictT = Counter(t)
        if len(dictS)!=len(dictT):
            return False
        for val in dictS.values():
            if val not in dictT.values():
                return False
        return True
        
# @lc code=end


#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST = defaultdict()
        mapTS = defaultdict()

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if c1 in mapST and mapST[c1]!=c2:
                return False
            if c2 in mapTS and mapTS[c2]!=c1:
                return False
            mapST[c1]=c2
            mapTS[c2]=c1
        return True
        
# @lc code=end


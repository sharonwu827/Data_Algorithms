#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t) :
            return False
        p1 = 0 
        p2 = 0 
        while p1<len(s) and p2<len(t):
            # we find a matching letter
            if t[p2] == s[p1]:
                p1+=1
                p2+=1
            else:
                p2+=1
        return p1==len(s)



       

        
        
# @lc code=end


#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1 = 0 
        l2 = 0 
        while l1<len(s) and l2<len(t):
            if s[l1]!=t[l2]:
                l2+=1
            else:
                l1+=1
                l2+=1
        return True if l1==len(s) else False

        
        
# @lc code=end


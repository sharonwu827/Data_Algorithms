#
# @lc app=leetcode id=1541 lang=python3
#
# [1541] Minimum Insertions to Balance a Parentheses String
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        i = 0
        res = 0 
        need+=2
        while i<len(s):
            if s[i]=='(':
                need+=2
            if s[i]==')':
                need-=1
        

                
                
                

        
# @lc code=end


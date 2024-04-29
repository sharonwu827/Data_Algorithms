#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0
        for i, char in enumerate(s):
            if char == '(':
                stack.append('(')
            else:
                if stack:
                    stack.pop()
                else:
                    res+=1
        if stack:
            res+=len(stack)
        return res

        
# @lc code=end


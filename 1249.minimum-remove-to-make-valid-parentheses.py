#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if not stack:
                    indexes_to_remove.add(i)
                else:
                    stack.pop()
        
        # Mark remaining unmatched opening parentheses
        for index in stack:
            indexes_to_remove.add(index)

        res = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                res.append(c)
        return "".join(res)
# @lc code=end


#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        res = []
        for i in range(k):
            while stack and s[i] >= s[stack[-1]]:
                stack.pop()
            stack.append(i)
        res.append(s[stack[0]])
        


        
# @lc code=end


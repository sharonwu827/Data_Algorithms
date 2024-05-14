#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        def backtrack(curLeft, curRight, path):
            if len(path) == n*2:
                self.res.append(''.join(path.copy()))
                return 
            if curLeft<n:
                path.append('(')
                backtrack(curLeft+1, curRight, path)
                path.pop()
            if curRight<curLeft:#注意这个条件
                path.append(')')
                backtrack(curLeft, curRight+1, path)
                path.pop()
        
        backtrack(0, 0, [])
        return self.res 


            

# @lc code=end


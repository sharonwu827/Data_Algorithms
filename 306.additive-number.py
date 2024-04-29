#
# @lc app=leetcode id=306 lang=python3
#
# [306] Additive Number
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(startInd, path):
            if startInd == len(num):
                return
            for i in range(startInd, len(num)):
                if i-startInd < 2:
                    dfs(i+1, path.append())
                else:
                    if 
                    

                    

            
            
        
# @lc code=end


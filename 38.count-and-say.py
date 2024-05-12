#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        curStr = '1'
        if n == 1:
            return '1'
        for _ in range(1, n):
            i = 0 
            j = 0
            nextStr = ''
            while i<len(curStr):
                while j<len(curStr) and curStr[i]==curStr[j]:
                    j+=1
                nextStr+=str(j-i)+curStr[i]
                i = j
            curStr = nextStr
        return curStr
''


                
                
        
# @lc code=end


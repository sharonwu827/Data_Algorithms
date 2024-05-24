#
# @lc app=leetcode id=2222 lang=python3
#
# [2222] Number of Ways to Select Buildings
#

# @lc code=start
class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)     
        n0 = s.count('0')
        n1 = n-n0

        cnt0 = 0 
        cnt1 = 0
        res = 0
        for i, char in enumerate(s):
            if char == '0':
                cnt0+=1
                res += cnt1*(n1-cnt1) 
            else:
                cnt1+=1
                res+= cnt0*(n0-cnt0)
        return res


        
# @lc code=end


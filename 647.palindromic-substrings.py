#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        res = 0 
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i]==s[j]:
                    if j-i<=2:
                        dp[i][j]= True
                    else:
                        dp[i][j]=dp[i+1][j-1]
                if dp[i][j]:
                    res+=1
        return res
                        




        


        
# @lc code=end


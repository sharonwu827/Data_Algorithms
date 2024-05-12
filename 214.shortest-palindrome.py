#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i]==s[j]:
                    if j-i<=2:
                        dp[i][j]= True
                    else:
                        dp[i][j]=dp[i+1][j-1]
                if not dp[i][j]:
                    if j-i<1:

        return res
        
# @lc code=end



        
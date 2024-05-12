#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        #dp[i][j]<-dp[i+1][j-1]
        dp = [[False]*n for _ in range(n)]
        maxLen = 1
        startInd = 0
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1,-1,-1):
            for j in range(i+1, n):
                if s[i]==s[j]: #aba
                    if j-i<=2:
                        dp[i][j]=True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j-i+1 > maxLen:
                    maxLen = j-i+1
                    startInd = i

        return s[startInd:startInd+maxLen]
                        
# @lc code=end


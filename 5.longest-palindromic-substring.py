#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        maxLen = 0
        startInd = 0
        for i in range(n):
            dp[i][i] = True
            
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] ==s[j]:
                    if j-i+1<=3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and maxLen < j-i+1:
                    maxLen = max(maxLen, j-i+1)
                    startInd = i

        return s[startInd:startInd+maxLen]

                    

       

# @lc code=end


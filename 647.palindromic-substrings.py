#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # dp[i][j]: whether the s[i:j+1] is the palindrome
        dp = [ [False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        res = 0
        # 从下到上，从左到右遍历
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] ==s[j]:
                    if j-i<=1:
                        dp[i][j] = True
                        res+=1
                    else:
                        if dp[i+1][j-1]==True:
                            dp[i][j] = True
                            res+=1
        return res



        
# @lc code=end


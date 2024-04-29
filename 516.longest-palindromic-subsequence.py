#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # dp[i][j]:  the longest length between s[i:j+1]
        dp = [ [0]* n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        # 注意这个循环方式
        # 因为是要从大区间推到小区间
        # 所以i从n-1倒着iterate
        # j必须比i小 s[i:j+1]才可以成立 iterate的方向是向j逼近
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1,j], dp[i][j-1])
        return dp[0][n-1]

        


        
# @lc code=end


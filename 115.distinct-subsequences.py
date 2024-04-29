#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len1 = len(s)
        len2 = len(t)
        # dp[i][j]: the number of subsequence between s[i-1]j[j-1]
        dp = [[0]*(len2+1) for _ in range(len1+1)]
        for i in range(len1+1):
            for j in range(len2+1):
                if s[i-1] == j[j-1]:
                    




                    

# @lc code=end


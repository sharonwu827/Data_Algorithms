#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        # dp[i][j]: 以下标i-1为结尾的字符串word1，和以下标j-1为结尾的字符串word2的最近编辑距离
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        for i in range(n1+1):
            dp[i][0] = i
        for j in range(n2+1):
            dp[0][j] = j
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1]==word2[j-1]: # 说明不用任何编辑 不操作
                    dp[i][j] = dp[i-1][j-1]
                # 需要编辑 增,删,换
                else:  
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        return dp[-1][-1]
        
# @lc code=end


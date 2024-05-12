#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        
        dp = [0] * n
        dp[0] = 1
        # 我们只关心i自己能否形成独立 item和i是否能够与（i-1）形成 item
        for i in range(1, n):
            # 可以自己形成item
            if s[i] != '0':
                dp[i] += dp[i - 1]
            # 可以和上一个字母形成item
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                #注意这个写法
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        return dp[n - 1]  
            
# @lc code=end


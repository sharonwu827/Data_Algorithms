#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        # if n<2:
        #     return n
        # dp = [0]*(n+1)
        # dp[0] = 0 
        # dp[1] = 1
        # for i in range(2, n+1):
        #     dp[i] = dp[i-1]+dp[i-2]
        # return dp[n]
        def dfs(n):
            if n<2:
                return n
            return dfs(n - 1) + dfs(n - 2)
            
        return dfs(n)
            


        
# @lc code=end


#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # dp[i][j]: from coins[:i-1], numbers of coins need to form j
        dp = [[float("inf")] * (amount+1) for _ in range(n+1)]
        for i in range(n):
            dp[i][0] = 0
        # dp[0][coins[0]] = 1 # 这个条件不能有
        for i in range(1, n+1):
            for j in range(amount+1):
                if coins[i-1]<=j:
                    # 因为硬币可以重复取，
                    # 所以当coins[i-1]<=j时，是从当前dp[i][j - coin]而不是dp[i - 1][j - coin]获取
                    # 因为dp[i][j - coin]已经包含了选取过coin的情况
                    dp[i][j] = min(dp[i-1][j],dp[i][j-coins[i-1]]+1)
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][amount] if dp[n][amount]!=float("inf") else -1
                    

            
    
# @lc code=end
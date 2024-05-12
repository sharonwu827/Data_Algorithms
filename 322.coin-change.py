#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # dp[i][j]：select from coin[:i-1] the fewest number of coins that need to make amount of j
        dp = [[float('inf')] * (amount+1) for _ in range(n+1)]
        # from coin[:i-1], the fewest number to conform package of 0
        # dp[0][0] = 0
        for i in range(n):
            dp[i][0] = 0 
        for i in range(1, n+1):
            for j in range(amount+1):
                if coins[i-1]>j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]]+1)
        return dp[-1][-1] if dp[-1][-1]!=float('inf') else -1
    
# @lc code=end
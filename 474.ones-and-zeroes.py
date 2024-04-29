#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        n = len(strs)
        # dp[i][j]: from strs[:i-1], thee 
        dp = [ [0] * (m+1) for _ in range(n+1)]
        
        





        
# @lc code=end


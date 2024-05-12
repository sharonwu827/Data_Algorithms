#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n ==1:
            return [-1]
        dp = [0]*n
        dp[-1] = -1
        dp[-2] = arr[-1]
        for i in range(n-3, -1, -1):
            dp[i] = max(arr[i+1], dp[i+1])
        return dp


        



        
        
        
# @lc code=end


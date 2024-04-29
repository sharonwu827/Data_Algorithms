#
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#

# @lc code=start
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [0]*n
        for i in range(3,n):
            for j in range(i):
                for k in range(j):
                    if arr[k]+arr[j]==arr[i]:
                        dp[i] = max(dp[i],  dp[j]+1)
        return max(dp)


        
# @lc code=end


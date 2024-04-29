#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#

# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
       
        '''
        1. dp[i][j]: nums1[:i-1] nums[:j-1] max len of repeated subarray
        2. dp[i][j] = dp[i-1][j-1]+1; when nums1[i] == nums2[j]
        
        '''
        
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[0]* (n2+1) for _ in range(n1+1)]
        max_len = -float("inf")
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                if dp[i][j]>max_len:
                    max_len = dp[i][j]
        return max_len




        
# @lc code=end


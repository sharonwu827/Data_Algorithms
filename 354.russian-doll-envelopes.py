#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x:(x[0], x[1]))
        n = len(envelopes)
        dp = [1] * n
        for i in range(1, n):
            if envelopes[i][0] > envelopes[i-1][0]:
                continue
            if envelopes[i][1] > envelopes[i-1][1]:
                # can fit now
                

        for i




        
       
        
        
# @lc code=end


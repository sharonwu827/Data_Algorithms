#
# @lc app=leetcode id=1751 lang=python3
#
# [1751] Maximum Number of Events That Can Be Attended II
#

# @lc code=start
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key = lambda x:x[1])
        n = len(events)
        takes = 0 

        dp = [0] * (n+1)
        for i in range(1, n+1):
            curStart = events[i-1][0]
            curVal =  events[i-1][-1]
            if takes < 2:
                # we are not taking current interval
                if dp[i-1]>= dp[k]+curVal:
                    dp[i] =dp[i-1]
               # we take current interval
                else:
                    dp[i] = dp[k]+curVal
                    takes+=1
            else:
                dp[i] =dp[i-1]
        return dp[n]
            

            
        
# @lc code=end


#
# @lc app=leetcode id=2008 lang=python3
#
# [2008] Maximum Earnings From Taxi
#

# @lc code=start
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key = lambda x:x[1])
        n = len(rides)
        dp = [0]*(n+1)

        def find_latest_non_overlap(curStart, curInd):
            # find the max index that have end time <= to curStart
            # find the min index that have end time > curStart
            # so we need to include curInd in right
            left = 0 
            right = curInd
            while left < right:
                mid = left+(right-left)//2
                if rides[mid][1] > curStart:
                    right = mid
                else:
                    left = mid+1
            return left-1 # min value that satisfy rides[left][2]>curStart:
        
        for i in range(1, n+1):
            curStart = rides[i-1][0]
            curProfit = rides[i-1][1] - rides[i-1][0] + rides[i-1][2]
            prev_job_index = find_latest_non_overlap(curStart, i-1)
            dp[i] = max(dp[i-1], dp[prev_job_index+1]+curProfit)
        return dp[n]
# @lc code=end


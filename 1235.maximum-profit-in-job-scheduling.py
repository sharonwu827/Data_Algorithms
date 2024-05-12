#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#




class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = []
        n = len(startTime)
        for i in range(n):
            intervals.append([startTime[i], endTime[i], profit[i]])
        # Sort based on end time
        intervals.sort(key=lambda x: x[1])

        # Function to find the latest non-overlapping job
        def find_latest_non_overlap(curInd, curStart, intervals):
            for i in range(curInd, -1, -1):
                if intervals[i][1]<=curStart:
                    return i
            return -1
                
        # Dynamic programming table to store the maximum profit at each index
        # 如果选当前工作，那么就要保证上一个工作的时间点不能和当前工作冲突
        # dp[i]=max(dp[i−1],dp[k]+profit[i−1])
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            curStart = intervals[i - 1][0]
            curEnd = intervals[i - 1][1]
            curProfit = intervals[i - 1][2]
            prev_job_index = find_latest_non_overlap(i - 1, curStart, intervals )
            dp[i] = max(dp[i-1], dp[prev_job_index] + curProfit)
        return dp[n]

# @lc code=end


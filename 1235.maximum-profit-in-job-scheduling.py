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
                
        # dp[i]: max start from interval 0 to interval i
        # dp[0]=0:表示没有兼职工作时报酬为 000
        # 如果选当前工作，那么就要保证上一个工作的时间点不能和当前工作冲突
        # dp[i]=max(dp[i−1], dp[j]+interval[i-1][-1]) 
        # so now we need to find the most recent j 第 i 份工作开始时间之前结束的最后一份工作
        
        def find_latest_non_overlap(curInd, curStart):
            # find the max index that have end time <= to curStart
            # find the min index that have end time > curStart
            # so we need to include curInd in right
            left = 0 
            right = curInd
            while left < right:
                mid = left+(right-left)//2
                if intervals[mid][1]>curStart:
                    right = mid
                else:
                    left = mid+1
            return left-1 
        
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            curStart = intervals[i - 1][0]
            curProfit = intervals[i - 1][2]
            prev_job_index = find_latest_non_overlap(i - 1, curStart)
            dp[i] = max(dp[i - 1], dp[prev_job_index + 1] + curProfit)
            # if prev_job_index != -1:
            #     dp[i] = max(dp[i - 1], dp[prev_job_index + 1] + curProfit)
            # else:
            #     dp[i] = max(dp[i - 1], curProfit)
        return dp[n]

# @lc code=end


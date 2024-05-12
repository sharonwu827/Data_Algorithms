#
# @lc app=leetcode id=1288 lang=python3
#
# [1288] Remove Covered Intervals
#

# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0], -x[1]))
        n = len(intervals)
        if n == 1:
            return 1
        curEnd = intervals[0][1]
        res = n
        for i in range(1, n):
            if intervals[i][1]<=curEnd:
                res-=1
            else:
                curEnd = intervals[i][1]
        return res




        
# @lc code=end


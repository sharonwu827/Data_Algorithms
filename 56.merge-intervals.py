#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key=lambda x:x[0])
        if n == 1:
            return intervals
        res = []
        curInt = intervals[0]
        for i in range(1, n):
            if curInt[1]>=intervals[i][0]:
                left = min(curInt[0], intervals[i][0])
                right = max(curInt[1], intervals[i][1])
                curInt = [left, right]
            else:
                res.append(curInt)
                curInt = intervals[i]
        res.append(curInt)
        return res



       
# @lc code=end


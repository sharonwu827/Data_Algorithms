#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res =[]
        for i in range(len(intervals)):
            if intervals[i][0]>newInterval[-1]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            elif intervals[i][1]<newInterval[0]:
                res.append(intervals[i])
            else:
                newStart = min(intervals[i][0], newInterval[0])
                newEnd = max(intervals[i][1], newInterval[1])
                newInterval = [newStart, newEnd]
        res.append(newInterval)
        return res




                

        
# @lc code=end


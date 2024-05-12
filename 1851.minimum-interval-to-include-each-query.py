#
# @lc app=leetcode id=1851 lang=python3
#
# [1851] Minimum Interval to Include Each Query
#

# @lc code=start
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x:(x[0],(x[1]-x[0])))
        def getShortestInt(num):
            curLen =  float('inf')
            for interval in intervals:
                if num>=interval[0] and num<=interval[1]:
                    curLen = min(curLen, interval[1]-interval[0]+1)
                
            return -1 if curLen == float('inf') else curLen
        
        res = []
        for q in queries:
            res.append(getShortestInt(q))
        return res


        
# @lc code=end


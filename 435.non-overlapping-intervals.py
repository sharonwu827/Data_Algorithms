#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[1]))
        n = len(intervals)
        if n == 1:
            return 0
        curEnd = intervals[0][-1]
        res = 0
        for i in range(1, n):
            if intervals[i][0]<curEnd:
                res+=1
            else:
                curEnd = intervals[i][-1]
        return res
                




        
# @lc code=end

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0]) # nlogn
        n = len(intervals)
        roomNeeded = 1
        # store the end time for each meeting room we currently have
        minHeap = [intervals[0][1]] 
        heapq.heapify(minHeap) #nlogn
        for i in range(1, n):
            if intervals[i][0]<minHeap[0]:
                roomNeeded += 1
                heapq.heappush(minHeap, intervals[i][1])
            else:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, intervals[i][1])
        return roomNeeded
    





       
            
                 




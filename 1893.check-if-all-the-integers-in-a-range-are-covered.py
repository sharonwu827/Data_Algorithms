#
# @lc app=leetcode id=1893 lang=python3
#
# [1893] Check if All the Integers in a Range Are Covered
#

# @lc code=start
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort(key = lambda x:x[0])
       
        curInt = ranges[0]
        if len(ranges) ==1:
            return curInt[0]<=left and curInt[1]>=right
        
        for i in range(1, len(ranges)):
            if ranges[i][0]<curInt[1] or ranges[i][0]-curInt[1]==1:
                curInt = [curInt[0], ranges[i][1]]
            else:
                curInt = ranges[i]
            if curInt[0]<=left and curInt[1]>=right:
                return True

        return False
            

        
# @lc code=end
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        minHeap = 0 
        heapq.heappush(minHeap, intervals[0][1])
        roomNeeded = 1

        for i in range(1, len(intervals)):
            if intervals[i-1][1]>intervals[i][0]:
                # if the room we current had have already end the meeting prior to current meeting start
                # we can use the current meeting room
                if minHeap[0] < intervals[i][0]:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, intervals[i][1])
                else:
                    roomNeeded+=1
                    heapq.heappush(minHeap, intervals[i][1])
        return roomNeeded

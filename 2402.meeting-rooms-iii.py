#
# @lc app=leetcode id=2402 lang=python3
#
# [2402] Meeting Rooms III
#

# @lc code=start
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x:x[0])
        heap = []
        heapq.heappush(heap, meetings[0][1])
        
        
        


        
# @lc code=end


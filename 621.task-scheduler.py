#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        cnt = Counter(tasks)
        for val in cnt.values():
            heapq.heappush(maxHeap, -val)
        intervals = 0 
        queue =deque() # store (-val, the interval the val can be processed again)

        while maxHeap or queue:
            intervals+=1
            if maxHeap:
                freq = heapq.heappop(maxHeap)
                if -freq>1:
                    queue.append((freq+1, intervals+n))
            if queue and queue[0][1] == intervals:
                remaining = queue.popleft()
                 # Check if the remaining interval is less than or equal to the current interval
                heapq.heappush(maxHeap, remaining[0])
    
        return intervals
                

        
                      
# @lc code=end


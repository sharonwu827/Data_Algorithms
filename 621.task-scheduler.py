#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasksCounter = Counter(tasks)
        maxHeap = []
        for key, freq in tasksCounter.items():
            heapq.heappush(maxHeap, (-freq, key))
        res = 0
        curTime = 0 
        temp = deque()
        while maxHeap or temp:
            curTime+=1
            if maxHeap:
                freq, key = heapq.heappop(maxHeap)
                if freq+1<0: 
                    temp.append((freq+1, key, curTime+n))
            if temp and temp[0][-1]<=curTime:
                freq, key, _ = temp.popleft()
                heapq.heappush(maxHeap, (freq, key))
        return curTime

            


            
            
            
            
            

        
        
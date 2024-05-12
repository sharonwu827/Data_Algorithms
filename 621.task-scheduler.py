#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if k==0 or k==1:
            return s
        dict_ = Counter(s)
        maxHeap = [] 
        queue = deque() 
        for char, freq in dict_.items():
            heapq.heappush(maxHeap, (-freq, char))
        res = []
         # Process tasks until the heap is empty
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            res.append(char)
            queue.append((freq+1, char))
            if len(queue)>=n:
                nextFreq, nextChar = queue.popleft()
                if next_freq < 0:
                    heapq.heappush(maxHeap, (nextFreq, nextChar))

        if len(res)<len(s):
            return ""
        else:
            return ''.join(res) 
        
#
# @lc app=leetcode id=1953 lang=python3
#
# [1953] Maximum Number of Weeks for Which You Can Work
#

# @lc code=start
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        maxHeap = []
        for i in range(len(milestones)):
            heapq.heappush(maxHeap, (-milestones[i], i)) # store (-#milestone, project)
        curTime = 0
        prevProject = None
        # res = []
        queue = deque()
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            curTime +=1
            queue.append((freq+1, char))
            if len(queue)>=2:
                nextFreq, nextChar = queue.popleft()
                if nextFreq < 0:
                    heapq.heappush(maxHeap, (nextFreq, nextChar))

        return curTime
                
# @lc code=end

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
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
            if len(queue)>=k:
                nextFreq, nextChar = queue.popleft()
                if next_freq < 0:
                    heapq.heappush(maxHeap, (nextFreq, nextChar))

        if len(res)<len(s):
            return ""
        else:
            return ''.join(res) 
                
                

            


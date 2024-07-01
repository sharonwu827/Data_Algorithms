class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        sCounter = Counter(s)
        maxHeap = []
        for key, freq in sCounter.items():
            heapq.heappush(maxHeap, (-freq, key))
        
        res = []
        curTime = 0 
        temp = deque()

        while maxHeap:
            curTime+=1
            if maxHeap:
                freq, key = heapq.heappop(maxHeap)
                res.append(key) 
                if freq+1<0: 
                    temp.append((freq+1, key, curTime+k))   
            if len(temp)>=k:
                freq, key, _ = temp.popleft()
                heapq.heappush(maxHeap, (freq, key))

        return "".join(res)

                
            
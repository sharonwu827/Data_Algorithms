#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
class Solution:
    def reorganizeString(self, s: str) -> str:
        sCounter =  Counter(s)
        maxHeap = []
        for key, freq in sCounter.items():
            heapq.heappush(maxHeap, (-freq, key))
        
        res = []
        while len(maxHeap)>=2:
            freq1, key1 = heapq.heappop(maxHeap)
            freq2, key2 = heapq.heappop(maxHeap)
            res.append(key1)
            res.append(key2)
            if freq1+1<0:
                heapq.heappush(maxHeap, (freq1+1, key1))
            if freq2+1<0:
                heapq.heappush(maxHeap, (freq2+1, key2))
        if maxHeap:
            if maxHeap[0][0]<-1:
                return ""
            else:
                res.append(maxHeap[0][1])
        return "".join(res)
        
            
        
#
# @lc app=leetcode id=1054 lang=python3
#
# [1054] Distant Barcodes
#

# @lc code=start
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        maxHeap = []
        cnt = Counter(barcodes)
        for key, freq in cnt.items():
            heapq.heappush(maxHeap, (-freq, key))
        res = []
        while len(maxHeap)>=2:
            freq1, key1 = heapq.heappop(maxHeap)
            freq2, key2 = heapq.heappop(maxHeap)
            res.extend([key1, key2])
            if -freq1>1:
                heapq.heappush(maxHeap, (freq1+1, key1))
            if -freq2>1:
                heapq.heappush(maxHeap, (freq2+1, key2))
        if len(maxHeap):
            res.append(maxHeap[0][1])
        return res

                
        
        
# @lc code=end


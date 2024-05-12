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
        for char, freq in cnt.items():
            heapq.heappush(maxHeap, (-freq, char))
        res = []
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            if res and res[-1] == char:
                # if not maxHeap:
                #     break
                nextFreq, nextChar = heapq.heappop(maxHeap)
                res.append(nextChar)
                if nextFreq+1<0:
                    heapq.heappush(maxHeap, (nextFreq+1, nextChar))
                heapq.heappush(maxHeap, (freq, char))
            else:
                 res.append(char)
                 if freq+1<0:
                    heapq.heappush(maxHeap, (freq+1, char))
        return res

                
        
        
# @lc code=end


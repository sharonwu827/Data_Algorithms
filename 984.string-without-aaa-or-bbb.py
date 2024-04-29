#
# @lc app=leetcode id=984 lang=python3
#
# [984] String Without AAA or BBB
#

# @lc code=start
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        maxHeap = []
        if a>0:
            heapq.heappush(maxHeap, (-a, 'a'))
        if b>0:
            heapq.heappush(maxHeap, (-b, 'b'))
        
        res = []
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            n = len(res)
            if n >=2 and res[-1]==res[-2]==char:
                nextFreq, nextChar = heapq.heappop(maxHeap)
                res.append(nextChar)
                if -nextFreq>1:
                    heapq.heappush(maxHeap, (nextFreq+1, nextChar))
                heapq.heappush(maxHeap, (freq, char))
            else:
                res.append(char)
                if -freq>1:
                    heapq.heappush(maxHeap, (freq+1, char))
        return ''.join(res)

                
        
        
# @lc code=end


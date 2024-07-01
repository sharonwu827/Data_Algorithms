#
# @lc app=leetcode id=1753 lang=python3
#
# [1753] Maximum Score From Removing Stones
#

# @lc code=start
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        maxHeap = []
        heapq.heappush(maxHeap, (-a, 'a'))
        heapq.heappush(maxHeap, (-b, 'b'))
        heapq.heappush(maxHeap, (-c, 'c'))
        
        res = 0 
        while len(maxHeap)>=2:
            freq1, key1 = heapq.heappop(maxHeap)
            freq2, key2 = heapq.heappop(maxHeap)
            res+=1
            if freq1+1<0: 
                heapq.heappush(maxHeap, (freq1+1, key1))
            if freq2+1<0: 
                heapq.heappush(maxHeap, (freq2+1, key2))
        return res
            
        
# @lc code=end


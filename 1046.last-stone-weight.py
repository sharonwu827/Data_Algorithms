#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#
import heapq
# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap)>=2:
            first, second = heapq.heappop(heap), heapq.heappop(heap)
            if first!= second:
                heapq.heappush(heap, first-second)
        return -heap[0] if len(heap) else 0
                


        
            

        
# @lc code=end


#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
import heapq
# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2,3,5]
        visited = set()
        visited.add(1)
        heap = [1]
        
        for i in range(n-1):
            cur = heapq.heappop(heap)
            for factor in factors:
                nxt = cur * factor
                if nxt not in visited:
                    heapq.heappush(heap, nxt)
                    visited.add(nxt)
        return heap[0]
        

        
# @lc code=end

